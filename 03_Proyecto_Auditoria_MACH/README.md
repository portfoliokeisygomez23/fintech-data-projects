# 📊 Proyecto Auditoría Interna - BCI MACH

## 🚨 Problemática 
* El proceso de validación de transacciones entre Payku y el banco BCI-MACH se realizaba de forma manual, lo que implicaba altos tiempos de procesamiento, riesgo de errores humanos y falta de trazabilidad.
* No existía un mecanismo automatizado o reporte que permitiera comparar diariamente las transacciones registradas en ambas fuentes ni detectar desviaciones oportunamente, afectando el control financiero y la capacidad de auditoría interna.


## 🎯 Objetivo
* Implementar una solución automatizada para la auditoría diaria de transacciones.
* Comparar las transacciones efectivas entre Payku y BCI-MACH.
* Detectar y alertar desviaciones de manera oportuna.
* Diseñar una arquitectura escalable basada en la nube.
* Centralizar la información para su análisis y visualización.


## ✅ Solución Implementada
Se implementó una solución end-to-end en la nube (Google Cloud) que automatiza la ingesta, almacenamiento, procesamiento y visualización de datos:

*	✔ Extracción automática de archivos adjuntos desde correo electrónico de BCI-MACH (Google Gmail).
*	✔ Carga de archivos a un Data Lake en la nube (Google Storage)
*	✔ Procesamiento e integración de datos en un Data Warehouse (Google BigQuery).
*	✔ Modelado y visualización en herramienta BI (PowerBI)
*	✔ Generación de alertas ante inconsistencias.

Esta solución elimina completamente la intervención manual en el proceso de auditoría.


## ✅ Arquitectura Implementada

![Arquitectura](../Imagenes/Diagrama_Mach.jpg)


## 🧩 Componentes de la Arquitectura

🔹 Ingesta de datos
* Recepción automática de archivos desde correo
* Procesamiento mediante Google Apps Script
* Validación inicial de archivos (envio de correo con la confirmación)

🔹 Almacenamiento (Data Lake)
* Uso de Google Cloud Storage
* Organización por carpetas (año-mes)
* Control de archivos duplicados (envio de correo con la alerta)

🔹 Procesamiento y analítica
* Carga automatizada a Google BigQuery
* Transformación y estructuración de datos
* Control de trazabilidad mediante tablas de control (envio de correo con la confirmación)

🔹 Consumo y visualización
* Integración con Microsoft Power BI
* Modelado de datos
* Generación de alertas por desviaciones
* Reportes analíticos por casuística
* Controles y automatizaciones clave
* Control de duplicados en Cloud Storage y BigQuery
* Trazabilidad completa de archivos procesados
* Notificaciones automáticas por correo (éxito, error, duplicados)
* Ejecución programada (procesamiento diario)


## 🚀 Gmail to BigQuery Automation Pipeline
Se automatizó el flujo de datos desde la bandeja de entrada de Gmail hacia Google BigQuery, utilizando Google Cloud Storage como capa de staging y validación.

**📋 Descripción del Flujo**
El proceso se divide en dos scripts principales que garantizan la integridad de los datos y evitan la duplicidad de archivos:

* 🐍 Script 1: Extracción y Carga (Gmail a GCS)

    * Escanea etiquetas o hilos específicos en Gmail.
    * Descarga el archivo adjunto.
    * Validación de Existencia: Antes de subir a Cloud Storage (GCS), el script verifica si el archivo ya existe en el bucket para evitar sobrescrituras accidentales o procesamientos duplicados.
    * El archivo correspondiente es: [Script1](../Scripts/FromGmailToStorage.py)

* 🐍 Script 2: Ingesta a Data Warehouse (GCS a BigQuery)
  
    * Detecta el nuevo archivo en GCS.
    * Ejecuta un Load Job hacia una tabla específica en BigQuery.
    * Maneja la detección de esquemas y la carga de datos.
    * El archivo correspondiente es: [Script2](../Scripts/FromStorageToBigQuery.py)

* Script 3: Permisos requeridos para activar e implemetar el pipeline
    * El archivo correspondiente es: [Script3](../Scripts/appsscript.json.txt)


## 💰 Costo de la implementación
La solución fue diseñada bajo un enfoque cost-efficient, aprovechando servicios serverless de GCP:

* Cloud Storage: costo bajo por almacenamiento (modelo pay-as-you-go).
* BigQuery: cobro por volumen de datos procesados/almacenados.
* Apps Script: sin costo adicional dentro del ecosistema Google Workspace.
* Power BI: costo asociado a licenciamiento existente.

Al no requerir infraestructura dedicada, se minimizan costos operativos y de mantenimiento. Y hasta ahora no supera los 5MM de registros tanto en Cloud Storage como BigQuery, siendo el costo menor a 10$ al mes.


## 🚀 Resultados
* ✔ Automatización completa del proceso de auditoría.
* ✔ Procesamiento diario de aproximadamente 500 mil de registros.
* ✔ Reducción significativa en tiempos de validación.
* ✔ Disponibilidad de información centralizada y actualizada.
* ✔ Detección oportuna de inconsistencias en transacciones.


## 💡 BENEFICIOS OBTENIDOS
* ✔ Eliminación de procesos manuales.
* ✔ Mejora en la calidad y confiabilidad de los datos.
* ✔ Mayor control y trazabilidad de la información.
* ✔ Escalabilidad de la solución.
* ✔ Visibilidad en tiempo casi real mediante dashboards.
* ✔ Capacidad de auditoría continua.


## 🛠️ Tecnologías Utilizadas
* Google Cloud Platform
* Google Apps Script
* Google Cloud Storage
* Google BigQuery
* Microsoft Power BI
* Python 3.8
* Gmail API: Lectura de correos y gestión de adjuntos.
* Google Cloud Storage SDK: Almacenamiento y validación de objetos.
* Google BigQuery SDK: Ingesta de datos a gran escala.
* REST APIs (OAuth 2.0 con Service Account)


