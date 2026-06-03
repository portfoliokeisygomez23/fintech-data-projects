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

## 🗺️ Estructura de Navegación y Reportes Incluidos

Como se detalla en el menú maestro de la aplicación, la suite está segmentada en 4 módulos analíticos críticos de alta densidad informativa:

### 📊 1. Módulo de Auditoría de Anulaciones

Este dashboard está diseñado para mitigar el riesgo financiero, identificar patrones de fraude y asegurar que cada transacción reversada se refleje de manera consistente en todo el ecosistema contable. Su valor técnico radica en la conciliación cruzada de tres orígenes de datos críticos, distribuidos en **3 páginas especializadas de navegación**:

---

### 🗂️ Estructura del Dashboard (Navegación en 3 Páginas)

#### Página 1: Conciliación Cruzada de Orígenes (Anulaciones vs. Liquidaciones)
* **Objetivo:** Asegurar que cada anulación procesada haya sido correctamente descontada del flujo de dispersión de fondos del comercio.
* **Lógica Analítica:** Cruce directo entre el maestro de transacciones revertidas y el módulo de liquidaciones. Permite identificar de forma proactiva si existen "fugas" de capital (ej. anulaciones aplicadas a nivel transaccional que por error de sistema continuaron en el flujo de pago hacia el cliente).
* **KPIs Core:** Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

#### Página 2: Conciliación Cruzada de Orígenes (Anulaciones vs. Monedero)
* **Objetivo:** Validar la consistencia de los balances de saldo (*Wallets*) ante eventos de reversa.
* **Lógica Analítica:** Compara la fecha y el monto estricto de la anulación contra los movimientos del monedero del usuario final o comercio. Certifica que el saldo disponible se actualice en tiempo real y con el monto exacto, evitando saldos negativos o duplicación de fondos tras un *chargeback* o cancelación.
* **Visualizaciones:** Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

#### Página 3: Análisis Granular por Comercio
* **Objetivo:** Identificar concentraciones de riesgo, anomalías operativas y comportamientos inusuales a nivel de cuentas individuales.
* **Lógica Analítica:** Agrupación e indexación de métricas de anulación discriminadas por ID de Cliente y Razón Social. Habilita al equipo de riesgo a detectar comercios con tasas de anulación inusualmente altas (*red flags* de fraude o problemas de integración técnica).
* **Componentes UX:** Tasa de Variación por Cliente y por Monto, Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

---

### 🧠 Ingeniería de Datos y Lógica DAX Aplicada

Para sostener este nivel de cruce multidimensional en memoria, el modelo semántico implementó las siguientes estrategias:

1. **Modelo Estrella de Conciliación:** Las tablas de hechos de *Anulaciones*, *Liquidaciones* y *Monedero* se relacionan indirectamente a través de dimensiones compartidas comunes (Dim_Cliente, Dim_Calendario y Dim_Transaccion_ID), evitando relaciones de muchos a muchos (*Many-to-Many*) que penalicen el rendimiento.
2. **Medidas de Control Bidireccional (DAX):** Se parametrizaron cálculos avanzados para detectar diferencias decimales o descalces temporales entre registros:

```dax
Monto_Discrepancia_Liquidacion = 
SUM(Anulaciones[Monto]) - CALCULATE(SUM(Liquidaciones[Monto_Descontado]))



### 2. Módulo de Auditoría de Liquidaciones
* **Enfoque:** Control, conciliación y validación de los procesos de pago y dispersión de fondos hacia los comercios de la plataforma.

### 3. Módulo de Auditoría Interna - Integración de Métodos de Pago Externos (Billeteras Digitales / Bancos)
* **Enfoque:** Conciliación externa y cuadratura de flujos transaccionales contra integraciones clave del ecosistema financiero local (ej. adquirentes y métodos prepago alternativos).

### 4. Módulo de Auditoría de Monedero
* **Enfoque:** Balance y trazabilidad de los saldos mantenidos en las billeteras internas, previniendo discrepancias contables en el core financiero.

![Menu](../Imagenes/menu_app.jpg)

---

## 🔄 Despliegue y Ciclo de Vida de la App
* **Frecuencia de Actualización:** Sincronizada con las actualizaciones automáticas individuales de cada modelo semánticos (Datasets).
* **Audiencia y Permisos:** Restringida sólo para la licencia Power BI correspondiente al Administrador. (Se evalúa comprar una licencia nueva para el area de Riesgo y Auditoría Interna)
* **Mantenimiento:** Los cambios impactan en la app y a los usuarios finales únicamente al presionar **"Actualizar Aplicación"**, garantizando un ambiente en producción libre de interrupciones o pruebas en vivo.
