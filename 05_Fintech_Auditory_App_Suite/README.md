# 📱 Aplicación Analítica: Suite de Auditoría Interna & Cumplimiento (Fintech)

## 📝 Descripción de la Solución
Esta documentación cubre el despliegue y empaquetamiento de la **Power BI App corporativa**, una solución analítica centralizada orientada al equipo de Control de Gestión, Riesgo y Auditoría Interna. 

En lugar de distribuir reportes aislados, se implementó una **Aplicación en Power BI Service** que unifica los esfuerzos de fiscalización operativa y financiera en un único entorno seguro, optimizando la experiencia de usuario (UX) mediante una navegación integrada y organizada por módulos de control.

---

## 🎯 Objetivos de la Aplicación (Gobernanza y UX)
* **Experiencia de Usuario Unificada:** Centralización de múltiples necesidades de auditoría bajo una misma interfaz de navegación vertical y colapsable (según se observa en la arquitectura de navegación de la suite).
* **Control de Accesos:** Distribución controlada a audiencias específicas dentro de la organización sin comprometer los permisos de edición del espacio de trabajo (*Workspace*).
* **Consistencia del Dato:** Todos los dashboards incluidos consumen modelos semánticos con actualización automatizada, garantizando que el equipo de auditoría trabaje siempre sobre la misma versión de la verdad.

---

## 🗺️ Estructura de Navegación y Reportes Incluidos

Como se detalla en el menú maestro de la aplicación (ver `image_945ca6.png`), la suite está segmentada en 4 módulos analíticos críticos de alta densidad informativa:

### 1. Modulo de Auditoría de Anulaciones
* **Enfoque:** Monitoreo preventivo y reactivo de transacciones reversadas, anuladas o sujetas a *chargebacks*.

### 2. Módulo de Auditoría de Liquidaciones
* **Enfoque:** Control, conciliación y validación de los procesos de pago y dispersión de fondos hacia los comercios de la plataforma.

### 3. Módulo de Auditoría Interna - Integración de Métodos de Pago Externos (Billeteras Digitales / Bancos)
* **Enfoque:** Conciliación externa y cuadratura de flujos transaccionales contra integraciones clave del ecosistema financiero local (ej. adquirentes y métodos prepago alternativos).

### 4. Módulo de Auditoría de Monedero / Cuenta Virtual
* **Enfoque:** Balance y trazabilidad de los saldos mantenidos en las billeteras internas, previniendo discrepancias contables en el core financiero.

---

## 🔄 Despliegue y Ciclo de Vida de la App
* **Frecuencia de Actualización:** Sincronizada con los pipelines automáticos individuales de cada modelo subyacente.
* **Audiencia y Permisos:** Restringida mediante Grupos de Seguridad de Azure AD a los roles de Auditoría Interna, Finanzas y C-Level.
* **Mantenimiento:** El desarrollo se realiza de forma aislada en el Workspace de desarrollo/producción. Los cambios impactan a los usuarios finales únicamente al presionar **"Actualizar Aplicación"**, garantizando un ambiente en producción libre de interrupciones o pruebas en vivo.
