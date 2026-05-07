function getLatestGmailAttachmentAndUploadToGCS() { 



  const archivosExitosos = [];
  const archivosFallidos = [];


  if (threads.length === 0) {
    Logger.log('⚠️ No se encontraron correos con adjuntos.');
    return;
  }

  // Ordenar hilos por fecha de último mensaje (descendente)
  threads.sort((a, b) => b.getLastMessageDate() - a.getLastMessageDate());
  const latestThread = threads[0];  // solo el más reciente
  const messages = latestThread.getMessages();
  const latestMessage = messages[messages.length - 1];  

  const attachments = latestMessage.getAttachments();
  if (attachments.length === 0) {
    Logger.log('📭 No hay adjuntos en el mensaje más reciente.');
    return;
  }

  const messageDate = new Date(latestMessage.getDate());
  const year = messageDate.getFullYear();
  const month = String(messageDate.getMonth() + 1).padStart(2, '0');

  const baseFolder = 'Banco1';  
  const folderName = `${year}-${month}`;

  for (const attachment of attachments) {
    const fileName = attachment.getName();
    const blob = attachment.copyBlob();
    const safeFileName = fileName.replace(/[^\w.-]/g, '_');
    const objectName = `${baseFolder}/${folderName}/${safeFileName}`;

    const url = `https://storage.googleapis.com/upload/storage/v1/b/${bucketName}/o?uploadType=media&name=${encodeURIComponent(objectName)}`;
    const options = {
      method: 'POST',
      contentType: blob.getContentType(),
      payload: blob.getBytes(),
      headers: {
        Authorization: 'Bearer ' + ScriptApp.getOAuthToken()
      },
      muteHttpExceptions: true
    };

try {
      const response = UrlFetchApp.fetch(url, options);
      const code = response.getResponseCode();
      const text = response.getContentText();

      if (code === 200 || code === 201) {
        Logger.log(`✅ Archivo subido: ${objectName}`);
        archivosExitosos.push(objectName);
      } else {
        Logger.log(`❌ Error al subir ${objectName}: [${code}] ${text}`);
  // Guarda una razón corta para el correo
        archivosFallidos.push(`${objectName} — HTTP ${code}: ${text.substring(0, 300)}`);
      }
    } catch (e) {
      Logger.log(`🚨 Excepción al subir ${objectName}: ${e.message}`);
      archivosFallidos.push(`${objectName} — Excepción: ${e.message}`);
    }

  }

// 📧 Enviar correo si hubo archivos subidos con éxito
if (archivosExitosos.length > 0) {
  GmailApp.sendEmail(
    emailDestino,
    "✅ Confirmación de carga a Google Cloud Storage",
    `Se han cargado correctamente los siguientes archivos en el bucket "${bucketName}":\n\n` +
    archivosExitosos.join("\n") +
    `\n\nFecha: ${new Date().toLocaleString()}`
  );
}

// 📧 Enviar correo si hubo archivos fallidos
if (archivosFallidos.length > 0) {
  GmailApp.sendEmail(
    emailDestino,
    "❌ Error al cargar archivos a Google Cloud Storage",
    `Los siguientes archivos NO se pudieron cargar al bucket "${bucketName}":\n\n` +
    archivosFallidos.join("\n") +
    `\n\nFecha: ${new Date().toLocaleString()}`
  );
}
}
