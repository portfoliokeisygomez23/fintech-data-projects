# 💳 Módulo de Auditoría Monedero (Trazabilidad Contable)

## 📝 Descripción del Módulo
Este módulo especializado audita el comportamiento, carga y consumo de los saldos mantenidos en las billeteras digitales internas (*Wallets*) de la plataforma. Su valor técnico radica en la implementación de un sistema de doble verificación temporal para asegurar el principio de integridad financiera: el balance de saldos no debe presentar descalces ni en el corte diario actual ni en la reconstrucción de la serie histórica.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

El reporte está estructurado estratégicamente en **2 páginas de navegación** que se dividen de la siguiente manera:

### Página 1: Consolidado del Día (Monitoreo de Alertas en Tiempo Real)
* **Enfoque:** Diagnóstico de salud financiera inmediata al abrir el dashboard.
* **Lógica Analítica:** Cruza los balances del Core de base de datos con los cierres de caja del día en curso. Aisla en una matriz de prioridad crítica cualquier cuenta o transacción que presente una discrepancia *hoy*, permitiendo al equipo de operaciones congelar saldos duplicados o corregir anomalías antes de los cierres contables del cierre de jornada.
* **KPIs Core:** Total Balance en Custodia Hoy, Alertas Activas de Descalce Diario, Monto Total en Discrepancia Actual, Número de Cuentas Virtuales Afectadas.

### Página 2: Detalle por Periodo de Tiempo (Trazabilidad Histórica)
* **Enfoque:** Consulta histórica flexible mediante selectores temporales dinámicos.
* **Lógica Analítica:** Permite reconstruir la línea de tiempo de cualquier cuenta o de la plataforma global mediante la fórmula de continuidad contable: 
  $$\text{Saldo Inicial} + \text{Abonos (Cash-In)} - \text{Cargos (Cash-Out)} = \text{Saldo Final}$$
  Habilita al auditor a viajar al pasado para rastrear en qué fecha exacta se originó una discrepancia histórica y comprobar si ya fue saneada o si aún persiste en los libros auxiliares.
* **Componentes UX:** Gráfico de líneas temporales para identificar tendencias de descalces y un buscador indexado por ID de Cliente para auditorías puntuales exhaustivas.

---

## 🧠 Lógica DAX e Ingeniería Aplicada

* **Cálculos de Balance Acumulado (Time Intelligence Avanzado):** Para evitar ralentizar el modelo en memoria con millones de registros de movimientos históricos, se implementaron medidas DAX optimizadas que calculan saldos en puntos específicos del tiempo de forma dinámica:

```dax
Saldo_Final_Historico = 
CALCULATE(
    SUM(Monedero[Monto_Movimiento]),
    FILTER(
        ALL('Dim_Calendario'),
        'Dim_Calendario'[Fecha] <= MAX('Dim_Calendario'[Fecha])
    )
)

```

---

## 🧠 Lógica DAX e Ingeniería Aplicada

* **Cálculos de Balance Acumulado (Time Intelligence):** Implementación de lógicas DAX avanzadas sin afectar el rendimiento para calcular saldos acumulados en puntos específicos del tiempo (*Snapshot Tables*).
* **Row-Level Security (RLS) Avanzado:** Enlace estricto del modelo con las dimensiones de seguridad para garantizar que los auditores solo accedan a los segmentos de cuentas de su respectiva competencia comercial.
