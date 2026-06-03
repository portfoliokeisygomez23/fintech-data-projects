# 💳 Módulo de Auditoría Monedero (Trazabilidad Contable)

## 📝 Descripción del Módulo
Este módulo especializado audita el comportamiento, carga y consumo de los saldos mantenidos en las billeteras digitales internas (*Wallets*) de la plataforma. Funciona como un libro mayor auxiliar que asegura la consistencia de los saldos a favor de los usuarios, separando la urgencia del monitoreo diario del análisis forense histórico.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

### Página 1: Consolidado del Día
* **Enfoque:** Diagnóstico de salud financiera inmediata e identificación de descalces en tiempo real al abrir el dashboard.
* **Lógica Analítica:** Cruza de forma automática los balances del Core de base de datos con los cierres de caja del día en curso. Permite al equipo de operaciones aislar al instante cualquier cuenta que presente discrepancias *hoy*, congelando saldos duplicados o corrigiendo anomalías de inmediato antes del cierre de jornada.
* **KPIs Core:** Total Balance en Custodia Hoy, Alertas Activas de Descalce Diario, Monto Total en Discrepancia Actual, Número de Cuentas Virtuales Afectadas.

### Página 2: Detalle por Periodo de Tiempo
* **Enfoque:** Verificación del principio de integridad financiera mediante la reconstrucción histórica de saldos: $\text{Saldo Inicial} + \text{Abonos} - \text{Cargos} = \text{Saldo Final}$.
* **Lógica Analítica:** Permite realizar consultas flexibles mediante selectores temporales dinámicos para viajar al pasado, rastrear en qué fecha exacta se originó un descalce histórico y comprobar de forma autónoma si la discrepancia persiste o si ya fue debidamente saneada.
* **KPIs Core:** Volumen Histórico en Custodia, Suma de Abonos (Cash-In), Suma de Débitos (Cash-Out), Descalces de Balance Acumulado.

---
