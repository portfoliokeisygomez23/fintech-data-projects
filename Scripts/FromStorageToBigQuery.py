

// Requiere token de autorización
function getOAuthToken() {
  return ScriptApp.getOAuthToken();
}

// Obtener el archivo CSV más reciente desde Cloud Storage
function getLatestCSVFile() {
  const url = `https://storage.googleapis.com/storage/v1/b/${BUCKET_NAME}/o?prefix=${PREFIX}`;
  
  const options = {
    method: 'get',
    headers: {
      Authorization: 'Bearer ' + getOAuthToken()
    },
    muteHttpExceptions: true
  };
  
  const response = UrlFetchApp.fetch(url, options);
  const files = JSON.parse(response.getContentText()).items;
  if (!files || files.length === 0) return null;
  
  // Ordenar por fecha de actualización
  files.sort((a, b) => new Date(b.updated) - new Date(a.updated));
  
  return files[0];  // Último archivo
}

// Cargar el archivo a BigQuery y enviar correo
function uploadLatestCSVToBigQuery() {
  const latestFile = getLatestCSVFile();
  if (!latestFile) {
    Logger.log('No se encontró ningún archivo CSV.');
    GmailApp.sendEmail(DEST_EMAIL, 'Carga Fallida - BigQuery', 'No se encontró ningún archivo CSV para cargar.');
    return;
  }

  const uri = `gs://${BUCKET_NAME}/${latestFile.name}`;
  const job = {
    configuration: {
      load: {
        sourceUris: [uri],
        destinationTable: {
          projectId: PROJECT_ID,
          datasetId: DATASET_ID,
          tableId: TABLE_ID
        },
        skipLeadingRows: 1,
        writeDisposition: 'WRITE_APPEND',
        sourceFormat: 'CSV',
        fieldDelimiter: ';',
        autodetect: true
      }
    }
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(job),
    headers: {
      Authorization: 'Bearer ' + getOAuthToken()
    },
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(
    `https://bigquery.googleapis.com/bigquery/v2/projects/${PROJECT_ID}/jobs`,
    options
  );

  const jobResponse = JSON.parse(response.getContentText());
  Logger.log("Job ID: " + jobResponse.jobReference.jobId);

  // Verificar si la carga fue aceptada por BigQuery

if (response.getResponseCode() === 200) {
  const jobResponse = JSON.parse(response.getContentText());

  if (jobResponse.status && jobResponse.status.errorResult) {
    // ❌ BigQuery aceptó el request pero falló al procesar
    GmailApp.sendEmail(
      DEST_EMAIL,
      'Error en Carga - BigQuery',
      `Ocurrió un error al cargar el archivo ${latestFile.name}.\n\n` +
      `Detalles del error:\n${JSON.stringify(jobResponse.status.errors, null, 2)}`
    );
  } else {
    // ✅ Éxito real
    GmailApp.sendEmail(
      DEST_EMAIL,
      '"✅ Carga Exitosa - BigQuery',
      `El archivo ${latestFile.name} se cargó correctamente en la tabla ${DATASET_ID}.${TABLE_ID}.\n\n` +
      `Job ID: ${jobResponse.jobReference.jobId}`
    );
  }

} else {
  // ❌ Error de red o autenticación
  GmailApp.sendEmail(
    DEST_EMAIL,
    'Error en Carga - BigQuery',
    `Ocurrió un error al enviar la solicitud.\n\nRespuesta: ${response.getContentText()}`
  );
}
}
