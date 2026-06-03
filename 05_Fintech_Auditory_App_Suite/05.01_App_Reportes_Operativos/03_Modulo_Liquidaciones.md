# 💰 Módulo de Auditoría de Liquidaciones (Gobernanza de Fondos)

## 📝 Descripción del Módulo
Este módulo especializado actúa como el motor de cuadratura para el proceso de *Payouts y PayIns* (dispersión de fondos) hacia los comercios. Su objetivo es garantizar la transparencia y exactitud en los pagos masivos mediante una conciliación interna de dos vías, verificando que cada lote de liquidación consolidado esté respaldado exactamente por el desglose de sus transacciones individuales aprobadas en la pasarela.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

### Página 1: Panel Único de Conciliación y Cuadratura de Lotes
* **Enfoque:** Monitoreo centralizado y de alta densidad para la validación de depósitos comerciales sin descalces financieros.
* **Lógica Analítica:** Cruza directamente la tabla de *Liquidaciones* (el monto total transferido o depositado) contra la tabla de *Transacciones* (la suma de los cobros individuales que componen ese pago). El dashboard despliega el listado maestro de liquidaciones y, al seleccionar una de ellas, permite al auditor ver el desglose completo de las ventas asociadas, exponiendo de forma inmediata si existe alguna transacción aprobada que quedó fuera del flujo de pago o si se liquidó un monto sin respaldo transaccional.
* **KPIs Core:** Total Fondos Liquidados, Volumen de Transacciones Asociadas, Tasa de Coincidencia de Lotes (Match Rate %), Monto Neto en Discrepancia.

![Liquidacion](../Imagenes/Liquidacion.jpg)

---

## 🧠 Lógica DAX e Ingeniería Aplicada

* **Modelo de Granularidad Mixta (Cabecera vs. Detalle):** Para resolver la diferencia de grano entre la tabla de Liquidaciones (un registro por depósito consolidado) y la tabla de Transacciones (millones de registros individuales), se estableció una relación de uno a varios (`1:N`) a través de una llave única de `Liquidacion_ID`. 

* **Métrica DAX de Validación de Integridad de Lote:** Se diseñó un cálculo dinámico que suma el campo neto de todas las transacciones vinculadas a un ID de liquidación y lo resta del monto reportado en la cabecera del depósito. Si la diferencia es cero ($0.00$), el lote se dictamina como "Consistente":

```dax
Descalce_Monto_Liquidado = 
SUM(Liquidaciones[Monto_Liquidado_Cabecera]) - CALCULATE(SUM(Transacciones[Monto_Neto_Transaccion]))

```


