# 🧾 Análisis de Documentos Tributarios (Auditoría Electrónica al SII)

## 📝 Resumen del Proyecto
Desarrollo de un ecosistema analítico en Power BI para el control, cruce y auditoría de documentos tributarios electrónicos (facturas, boletas, notas de crédito) enviados al **Servicio de Impuestos Internos (SII)**. El proyecto transforma logs de datos semiestructurados y registros planos en un tablero dinámico que permite monitorear montos totales, volúmenes de emisión y comportamiento transaccional (Ingresos vs. Egresos) por tipo de comercio.

## 🎯 El Reto Técnico
El principal desafío de este proyecto radicaba en la compleja estructura de los datos en origen (provenientes de una única tabla transaccional), presentando las siguientes problemáticas:

1. **Datos en la misma fila (Columnas Cruzadas):** Los registros de ingresos y egresos venían acoplados horizontalmente en la misma fila (ej: `folio_ingreso`, `folio_egreso`, `monto_ingreso`, `monto_egreso`), impidiendo un análisis de series de tiempo nativo.
2. **Información Anidada (String Arrays):** El detalle financiero crítico (Monto, IVA, etc.) venía encapsulado dentro de respuestas de servicios en formato de texto plano/array de PHP (`request_ingreso`, `request_egreso`).
3. **Requerimiento de Exportación:** El equipo operativo requería tanto la vista macro de KPIs como un módulo de "grano fino" para descargar listados masivos a Excel sin degradar el rendimiento del modelo.

---

## 🏗️ Solución Arquitectónica e Ingeniería de Datos

Para resolver la complejidad del origen, se diseñó un pipeline de transformación de datos en **Power Query (M)** y **DAX** estructurado en las siguientes etapas:

### 1. Desacople y Normalización (Estrategia de Append)
En lugar de trabajar con la tabla plana original (que estresaba el modelo), se optó por una arquitectura de bifurcación y consolidación:
* **Segmentación:** Se crearon dos consultas independientes apuntando al mismo origen: una especializada exclusivamente en **Ingresos** y otra en **Egresos**, aislando sus columnas correspondientes.
* **Consolidación (Append):** Se ejecutó una operación de anexado (*Append*) para unificar ambas consultas en una **única tabla consolidada de hechos**, transformando el modelo horizontal en un modelo vertical óptimo para analítica.

### 2. Extracción de Datos Semi-Estructurados (Parsing en Power Query)
Para abrir los arrays de PHP y extraer los valores tributarios sin recurrir a procesos pesados de backend, se implementaron funciones avanzadas de manipulación de texto en Power Query para delimitar y tipificar los campos ocultos en la columna `response_webservice`:

```powerquery
// Extracción dinámica del folio tributario desde el string/array
Number.FromText(
    Text.BetweenDelimiters([response_webservice], "[folio] => ", "#(lf)")
)
