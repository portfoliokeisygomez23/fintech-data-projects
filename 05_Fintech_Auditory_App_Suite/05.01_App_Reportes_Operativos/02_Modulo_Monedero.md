# 💳 Módulo de Monedero (Trazabilidad Contable)

## 📝 Descripción del Módulo
Este módulo especializado audita el comportamiento, carga y consumo de los saldos mantenidos en las billeteras digitales internas (*Wallets*) de la plataforma. Funciona como un libro mayor auxiliar que asegura la consistencia de los saldos a favor de los usuarios.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

### Página 1: Auditoría de Saldos y Continuidad Contable
* **Enfoque:** Verificación del principio de integridad financiera.
* **Lógica Analítica:** Ejecuta un cálculo histórico secuencial para comprobar que el saldo actual reportado por la base de datos coincida exactamente con la sumatoria matemática de sus movimientos históricos, detectando anomalías o inyecciones de saldo no autorizadas.
* **KPIs Core:** Volumen Total en Custodia, Suma de Abonos (Cash-In), Suma de Débitos (Cash-Out), Descalces de Balance.

### Página 2: Alertas Preventivas de Riesgo
* **Enfoque:** Detección de cuentas virtuales con comportamiento fuera de norma.
* **Lógica Analítica:** Muestra perfiles de usuarios con saldos negativos inexplicables, cuentas inactivas con saldos retenidos altos y picos inusuales de movimientos rápidos de dinero (*Velocity Checks*).

---

## 🧠 Lógica DAX e Ingeniería Aplicada

* **Cálculos de Balance Acumulado (Time Intelligence):** Implementación de lógicas DAX avanzadas sin afectar el rendimiento para calcular saldos acumulados en puntos específicos del tiempo (*Snapshot Tables*).
* **Row-Level Security (RLS) Avanzado:** Enlace estricto del modelo con las dimensiones de seguridad para garantizar que los auditores solo accedan a los segmentos de cuentas de su respectiva competencia comercial.
