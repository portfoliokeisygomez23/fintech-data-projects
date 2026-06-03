# 🔌 Módulo de Auditoría Interna - Integración MACH (Conciliación Externa)

## 📝 Descripción del Módulo
Este módulo especializado actúa como el motor de cuadratura externa para los flujos transaccionales de la integración corporativa con la billetera/adquirente MACH. A diferencia de un reporte convencional, esta solución es la capa de visualización final de una arquitectura **Serverless end-to-end en Google Cloud Platform (GCP)**, diseñada para transformar un proceso masivo de conciliación manual en un sistema automatizado de gestión por excepción.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

El diseño de la interfaz de usuario (UI/UX) está desarrollado para guiar al auditor desde una perspectiva macro (KPIs de negocio y descalces globales) hasta un nivel analítico granular (detalle registro por registro), dividiéndose en 2 páginas de navegación principales:

### Página 1: Monitor de KPIs - Conciliación Externa (Banco Adquirente vs. Fintech)
* **Enfoque:** Panel de control ejecutivo y operacional que mapea el flujo del dinero y clasifica de manera inteligente los estados de cuadratura de las transacciones recaudadas.
* **Lógica Analítica (Flujo Maestro):** Muestra un embudo comparativo directo de tres bloques: Total Recaudado por Adquirente Externo vs. Total Recaudado por la Fintech $\rightarrow$ derivando de forma automática en un bloque crítico de Inconsistencias / Diferencias (Diferencia de Monto y Diferencia en Cantidad de Transacciones).
* **Segmentación Inteligente por Casuísticas:** Reemplaza la auditoría tradicional por un bloque de control enfocado en 4 escenarios operacionales con botones de navegación integrados (Click para ver detalle):
  * **Casuística 1 (Efectiva/Efectiva):** Transacciones exitosas en el adquirente que se registraron correctamente como efectivas en el Core (Estatus = 1).
  * **Casuística 2 (Alerta Crítica):** Transacciones efectivas en el adquirente que figuran como "No Procesadas" en el Core (Estatus = 0). Representa el principal indicador de reclamos de clientes.
  * **Casuística 3 (Alerta de Riesgo):** Transacciones fallidas en el adquirente que por error de sincronización se registraron como efectivas (Estatus = 1) en el Core de la Fintech.
  * **Casuística 4 (Consistente):** Transacciones fallidas en la Fintech que correctamente no registran abonos en el procesador externo.

![mach](/Imagenes/mach.jpg)

### Página 2: Detalle de Transacciones Cruzadas (Vista de Coincidencias)
* **Enfoque:** Tabla espejo transaccional de alta densidad informativa para la validación forense de registros específicos.
* **Lógica Analítica:** Una vez que el usuario filtra por un rango de fechas mediante el segmentador dinámico, la página despliega en paralelo dos grillas maestras: el Detalle de Transacciones del Adquirente (incluyendo fecha, identificador único, montos, comisiones y el flag de validación DAX) y, justo debajo, el Detalle de Transacciones de la Fintech con sus respectivos atributos de cliente, orden y concepto. Esto permite una auditoría visual inmediata y una exportación limpia de datos en caso de disputas.

![mach2](/Imagenes/mach2.jpg)

---

## 🧠 Lógica de Ingeniería de Datos y Estrategia de BI (Big Data)

Para sostener este nivel de procesamiento con cargas superiores a los **500,000 registros diarios** sin degradación de rendimiento, se aplicaron las siguientes estrategias de arquitectura:

* **Estrategia de Almacenamiento Híbrido (Composite Model):** Se implementó un modelo semántico desacoplado que combina el modo **Import** (para dimensiones de alta velocidad y filtros) con **DirectQuery** conectado de forma nativa a Google BigQuery. Esto permite interrogar el histórico total de transacciones en la nube sin necesidad de saturar la memoria local del servidor de Power BI.
* **Procesamiento Delegado al Data Warehouse:** Se diseñaron **vistas pre-procesadas en BigQuery** para realizar las transformaciones complejas en la nube. De esta forma, Power BI solo consume datos optimizados, acelerando los tiempos de respuesta del dashboard a segundos.
* **Conciliación Automatizada en DAX:** Se sustituyó la revisión por planillas mediante métricas dinámicas en DAX encargadas de calcular las diferencias operacionales de manera instantánea:

```dax
Diferencia_Conciliacion_MACH = 
SUM(Core_Transacciones[Monto_Bruto]) - CALCULATE(SUM(Reporte_MACH[Monto_Transaccion]))

```

* **Gobernanza Automatizada:** Al estar acoplado al pipeline serverless en GCP (Gmail API $\rightarrow$ Cloud Storage $\rightarrow$ BigQuery), el modelo semántico garantiza consistencia absoluta, control de duplicados e integridad del 100% en las conciliaciones contables presentadas en la suite de la aplicación.
