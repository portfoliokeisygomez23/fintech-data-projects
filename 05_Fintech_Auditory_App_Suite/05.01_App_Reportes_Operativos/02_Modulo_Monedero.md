# 💳 Módulo de Auditoría Monedero (Trazabilidad Contable)

## 📝 Descripción del Módulo
Este módulo especializado audita de forma interna el comportamiento, carga y consumo de los saldos mantenidos en las billeteras digitales (*Wallets*) de la plataforma a través de la propia tabla de movimientos de monedero. Funciona como un mecanismo de control de integridad transaccional para asegurar que cada abono y egreso se sume o reste de manera matemáticamente exacta respecto al balance inmediatamente anterior.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

### Página 1: Consolidado del Día
* **Enfoque:** Diagnóstico de salud financiera inmediata e identificación de descalces en los saldos del día en curso al abrir el dashboard.
* **Lógica Analítica:** Evalúa los cierres de caja de la jornada actual. Permite al equipo de operaciones aislar al instante cualquier cuenta cuya sumatoria de movimientos del día no coincida con el balance final reportado *hoy*, congelando saldos duplicados o corrigiendo anomalías de inmediato antes del cierre de jornada.
* **KPIs Core:** Total Balance en Custodia Hoy, Alertas Activas de Descalce Diario, Monto Total en Discrepancia Actual, Número de Cuentas Virtuales Afectadas.
  
![monedero_consolidado](/Imagenes/monedero_consolidado.jpg)

### Página 2: Detalle por Periodo de Tiempo
* **Enfoque:** Verificación del principio de continuidad contable y auditoría mediante la reconstrucción de la serie de tiempo: $\text{Balance Anterior} + \text{Ingreso} - \text{Egreso} = \text{Balance Actual}$.
* **Lógica Analítica:** Permite realizar consultas flexibles mediante selectores temporales dinámicos para viajar al pasado y evaluar si históricamente el flujo de ingresos y egresos impactó correctamente el saldo acumulado. Habilita al auditor a detectar la fecha exacta en la que un movimiento rompió la secuencia lógica del saldo para identificar errores de sistema o alteraciones.
* **KPIs Core:** Volumen Histórico en Custodia, Suma de Ingresos, Suma de Egresos, Descalces de Balance Acumulado.

![monedero_detalle](/Imagenes/monedero_detalle.jpg)

---

## 🧠 Lógica DAX e Ingeniería Aplicada

* **Auditoría de Continuidad Secuencial (DAX):** Para validar que cada fila sume bien con el balance anterior, se diseñaron medidas DAX de acumulación temporal. Estas recalculan el saldo teórico esperado de la billetera hasta el momento exacto de la transacción y lo comparan contra el saldo registrado en la base de datos para exponer diferencias:

```dax
Saldo_Teorico_Acumulado = 
CALCULATE(
    SUM(Monedero[Monto_Ingreso]) - SUM(Monedero[Monto_Egreso]),
    FILTER(
        ALL('Dim_Calendario'),
        'Dim_Calendario'[Fecha] <= MAX('Dim_Calendario'[Fecha])
    )
)
