# 📱 Aplicación Analítica: Suite de Auditoría Interna & Cumplimiento (Fintech)

## 📝 Descripción de la Solución
Esta documentación cubre el despliegue y empaquetamiento de la **Power BI App corporativa**, una solución analítica centralizada orientada al equipo de Control de Gestión, Riesgo y Auditoría Interna. 

En lugar de distribuir reportes aislados, se implementó una **Aplicación en Power BI Service** que unifica los esfuerzos de auditorías operativas y financieras en un único entorno seguro, optimizando la experiencia de usuario (UX) mediante una navegación integrada y organizada por módulos de control.

---

## 🎯 Objetivos de la Aplicación (Gobernanza y UX)

* **Experiencia de Usuario Unificada:** Centralización de múltiples necesidades de auditoría bajo una misma interfaz de navegación vertical y colapsable (según se observa en la arquitectura de navegación de la suite).
* **Control de Accesos:** Distribución controlada a audiencias específicas dentro de la organización sin comprometer los permisos de edición del espacio de trabajo (*Workspace*).
* **Consistencia del Dato:** Todos los dashboards incluidos consumen modelos semánticos con actualización automatizada, garantizando que el equipo de auditoría trabaje siempre sobre la misma versión de la verdad.

---

## 🗺️ Módulos Analíticos e Interfaz de la Suite

La aplicación unifica el control financiero y operativo a través de 4 módulos especializados, diseñados con un enfoque de conciliación multidimensional y alertas necesarias para el análisis:

![Menu](../Imagenes/menu_app.jpg)

* **🚀 Módulo de Anulaciones (Mitigación de Riesgo):** Centraliza y audita las transacciones reversadas mediante un modelo de conciliación cruzada de tres vías (*Anulaciones vs. Liquidaciones vs. Monedero*). Su objetivo principal es detectar fugas de capital y automatizar las alertas por descalces en las cuentas de los comercios.
  
* **💰 Módulo de Liquidaciones (Gobernanza de Fondos):** Dedicado al control, tracking y validación del flujo de dispersión de capital hacia los comercios. Asegura la trazabilidad de los montos netos a pagar, comisiones descontadas y cumplimiento de los plazos de pago (*payouts*).
  
* **🔌 Módulo de Integración de Pagos (Conciliación Externa con Banco Emisor):** Realiza la cuadratura y validación de las transacciones procesadas contra los reportes de adquirentes externos, redes bancarias y billeteras digitales. Diseñado para identificar discrepancias en las pasarelas de pago de forma oportuna.
  
* **💳 Módulo de Monedero (Trazabilidad Contable):** Audita el comportamiento y balance de los saldos internos integrados en la plataforma. Su enfoque garantiza la consistencia del pasivo financiero de la empresa, evitando duplicidad de fondos o saldos negativos colaterales.
  
---

### 🧠 Ingeniería de Datos y Lógica DAX Aplicada

Para sostener este nivel de cruce multidimensional en memoria, el modelo semántico implementó las siguientes estrategias:

1. **Modelo Estrella de Conciliación:** Las tablas de hechos de *Anulaciones*, *Liquidaciones* y *Monedero* se relacionan indirectamente a través de dimensiones compartidas comunes (Dim_Cliente, Dim_Calendario y Dim_Transaccion_ID, etc.), evitando relaciones de muchos a muchos (*Many-to-Many*) que penalicen el rendimiento.
2. **Medidas de Control Bidireccional (DAX):** Se parametrizaron cálculos avanzados en DAX para detectar diferencias decimales o descalces temporales entre registros:

```dax
Monto_Discrepancia_Liquidacion = 
SUM(Anulaciones[Monto]) - CALCULATE(SUM(Liquidaciones[Monto_Descontado]))

```

---

## 🔄 Despliegue y Ciclo de Vida de la App
* **Frecuencia de Actualización:** Sincronizada con las actualizaciones automáticas individuales de cada modelo semánticos (Datasets).
* **Audiencia y Permisos:** Restringida sólo para la licencia Power BI correspondiente al Administrador. (Se evalúa comprar una licencia nueva para el area de Riesgo y Auditoría Interna)
* **Mantenimiento:** Los cambios impactan en la app y a los usuarios finales únicamente al presionar **"Actualizar Aplicación"**, garantizando un ambiente en producción libre de interrupciones o pruebas en vivo.
