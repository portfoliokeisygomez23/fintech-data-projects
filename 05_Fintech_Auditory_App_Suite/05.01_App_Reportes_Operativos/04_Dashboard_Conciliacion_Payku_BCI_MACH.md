# 🔌 Módulo de Auditoría Interna - Integración MACH (Conciliación Externa)

## 📝 Descripción del Módulo
Este módulo especializado actúa como el motor de cuadratura externa para los flujos transaccionales de la integración corporativa con la billetera/adquirente MACH. A diferencia de un reporte convencional, esta solución es la capa de visualización final de una arquitectura **Serverless end-to-end en Google Cloud Platform (GCP)**, diseñada para transformar un proceso masivo de conciliación manual en un sistema automatizado de gestión por excepción.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

El diseño de la interfaz está optimizado para procesar grandes volúmenes de datos transaccionales, estructurándose en las siguientes lógicas de control:

### 1. Panel de Cuadratura y Tasa de Coincidencia (Match Rate)
* **Enfoque:** Monitoreo analítico diario y control de semáforos para identificar discrepancias financieras entre ambas plataformas de forma inmediata.
* **Lógica Analítica:** Cruza en paralelo los registros aprobados de la Fintech (alojados en BigQuery) contra las cartolas de liquidación enviadas por MACH. Clasifica de manera automática cada transacción en tres estados críticos de auditoría: 
  * *Conciliadas:* Coincidencia exacta del identificador y monto.
  * *Faltantes en Core:* Cobros ejecutados por MACH no impactados internamente.
  * *Faltantes en Adquirente:* Ventas aprobadas en nuestra plataforma pero no liquidadas por el procesador externo.
* **KPIs Core:** Tasa de Match (%), Monto Total Conciliado, Volumen en Descalce Financiero, Alertas de Transacciones Huérfanas.

### 2. Gestión por Excepción y Deltas de Comisiones
* **Enfoque:** Diagnóstico operativo y financiero enfocado exclusivamente en variaciones o discrepancias (*Deltas*).
* **Lógica Analítica:** Desglosa los montos brutos e identifica desviaciones en la aplicación de tasas comerciales y comisiones. El sistema resalta automáticamente mediante alertas visuales aquellos registros con diferencias matemáticas, permitiendo al auditor ignorar los miles de registros correctos y actuar con foco únicamente donde existe un descalce.

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
