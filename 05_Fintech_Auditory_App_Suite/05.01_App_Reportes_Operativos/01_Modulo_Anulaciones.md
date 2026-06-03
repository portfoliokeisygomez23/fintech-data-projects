# 💳 Módulo de Auditoría de Anulaciones

## 📝 Descripción del Módulo

Este dashboard está diseñado para mitigar el riesgo financiero, identificar patrones de fraude y asegurar que cada transacción reversada se refleje de manera consistente en todo el ecosistema contable. Su valor técnico radica en la conciliación cruzada de tres orígenes de datos críticos, distribuidos en **3 páginas especializadas de navegación**:

---

### 🗂️ Estructura del Dashboard (Navegación en 3 Páginas)

#### Página 1: Conciliación Cruzada de Orígenes (Anulaciones vs. Liquidaciones)
* **Objetivo:** Asegurar que cada anulación procesada haya sido correctamente descontada del flujo de dispersión de fondos del comercio.
* **Lógica Analítica:** Cruce directo entre el maestro de transacciones revertidas y el módulo de liquidaciones. Permite identificar de forma proactiva si existen "fugas" de capital (ej. anulaciones aplicadas a nivel transaccional que por error de sistema continuaron en el flujo de pago hacia el cliente).
* **KPIs Core:** Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

![Auditoria_Liquidaciones](/Imagenes/Auditoria_Liquidaciones.jpg)

#### Página 2: Conciliación Cruzada de Orígenes (Anulaciones vs. Monedero)
* **Objetivo:** Validar la consistencia de los balances de saldo (*Wallets*) ante eventos de reversa.
* **Lógica Analítica:** Compara la fecha y el monto estricto de la anulación contra los movimientos del monedero del usuario final o comercio. Certifica que el saldo disponible se actualice en tiempo real y con el monto exacto, evitando saldos negativos o duplicación de fondos tras un *chargeback* o cancelación.
* **Visualizaciones:** Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

![Auditoria_Monedero](/Imagenes/Auditoria_Monedero.jpg)

#### Página 3: Análisis Granular por Comercio
* **Objetivo:** Identificar concentraciones de riesgo, anomalías operativas y comportamientos inusuales a nivel de cuentas individuales.
* **Lógica Analítica:** Agrupación e indexación de métricas de anulación discriminadas por ID de Cliente y Razón Social. Habilita al equipo de riesgo a detectar comercios con tasas de anulación inusualmente altas (*red flags* de fraude o problemas de integración técnica).
* **Componentes UX:** Tasa de Variación por Cliente y por Monto, Tasa de Coincidencia de Conciliación, Monto Total en Discrepancia, Alertas.

![Auditoria_Clientes](/Imagenes/Auditoria_Clientes.jpg)

---
