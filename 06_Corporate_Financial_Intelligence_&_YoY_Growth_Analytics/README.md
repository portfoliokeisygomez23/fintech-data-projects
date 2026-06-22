# 📊 Módulo de Estadística Anual (Análisis de Crecimiento & Inteligencia Temporal)

## 📝 Descripción del Módulo
Este módulo analítico está diseñado para proporcionar al equipo directivo (C-Level) y Control de Gestión una visión estratégica y macro de la evolución financiera del negocio. Su objetivo técnico es implementar lógicas de **Inteligencia Temporal (Time Intelligence)** para evaluar el rendimiento anual transaccional de manera comparativa frente al año anterior (Year-over-Year), permitiendo identificar estacionalidades, crecimiento real de comisiones y rendimiento por pasarelas de pago.

---

## 🗂️ Estructura del Dashboard y Capas Analíticas

El diseño visual aprovecha un esquema jerárquico de navegación y paneles informativos organizados que guían la interpretación financiera a través de tres áreas clave de análisis (conforme a las evidencias técnicas en `Parte1.jpg`, `Parte2.jpg` y `Parte3.jpg`):

### 1. Panel de Control Ejecutivo y Líneas de Evolución Temporal (Parte1.jpg)
* **Enfoque:** Monitoreo inmediato de métricas de rendimiento agrupadas por el año seleccionado mediante segmentadores interactivos dinámicos (2024, 2025, 2026).
* **Tarjetas de KPI Primarias con Alertas Visuales:** Cada bloque principal compara el rendimiento acumulado contra el año anterior (YoY), desplegando desviaciones porcentuales y formatos condicionales basados en íconos de alerta:
  * **Total Monto Transaccionado:** Volumen bruto procesado por la plataforma.
  * **Total Comisión:** Ingresos brutos generados a partir de las comisiones cobradas.
  * **Total Monto Final:** Liquidaciones y flujos netos finales resultantes.
  * **Tasa de Crecimiento Anual de Comisiones:** Porcentaje del delta acumulado YoY.
* **Líneas de Tendencia Evolutiva:** Bloque inferior con tres gráficos de líneas paralelas que contrastan el comportamiento mes a mes del Año Actual (Línea Continua) contra el Año Anterior (Línea Punteada) para los tres frentes clave: *Total Comisión, Total Monto y Total Monto Final*.

### 2. Capa de Métodos de Pago, Volumen y Promedios (Parte2.jpg)
* **Enfoque:** Análisis de penetración de mercado y ticket promedio por canal de recaudación.
* **Comparativa de Cantidad de Transacciones:** Gráfico de columnas apiladas mensuales que muestra visualmente la proporción del volumen transaccional ejecutado entre el periodo actual y el año anterior.
* **Comparativa de Promedio Monto Transaccionado:** Gráfico de líneas que expone la evolución del ticket promedio mensual del negocio, identificando si los picos de facturación responden a un aumento del valor transaccional o del volumen neto de operaciones.
* **Rendimiento por Métodos de Pago (vs. Año Anterior):** Gráfico de barras horizontales 100% apiladas que clasifica la participación y cuota de mercado de cada canal integrado (Webpay plus, MACH, Fintoc, ETpay, Khipu, Pago46, Floid, Hites, Transacción completa, ServiFacil), revelando variaciones en la preferencia del usuario en periodos YoY.

### 3. Matriz de Crecimiento Anual Neto (Parte3.jpg)
* **Enfoque:** Reporte de variaciones marginales para control financiero de comisiones efectivas.
* **Lógica Analítica:** Un gráfico de columnas en cascada enfocado exclusivamente en la **Tasa de Crecimiento Anual de la Comisión Efectiva agrupada por Mes**. Utiliza un formato de color semafórico condicional automático para resaltar los meses con crecimiento positivo (Azul) y aquellos con contracciones o variaciones negativas (Rojo) frente al mismo mes del año anterior.

---

## 🧠 Lógica DAX e Ingeniería Aplicada

Para sostener el dinamismo temporal y las comparaciones cruzadas de años, se implementaron medidas avanzadas dentro del modelo semántico compartimentado. A continuación, se desglosan los espacios para las fórmulas aplicadas en los KPIs del reporte:

### 1. Fórmulas de Inteligencia Temporal (Time Intelligence)

* **Monto Transaccionado del Año Anterior (LY):**
```dax
Fórmula DAX utilizada para calcular el monto transaccionado del año anterior:
TotalMontoTotalAñoAnterior = CALCULATE(sum(Transacciones[montofinal]), SAMEPERIODLASTYEAR(Calendario[Date]))
```

* **Comisión Acumulada del Año Anterior (LY):**
```dax
// COMPLETAR: Insertar aquí la fórmula DAX utilizada para calcular la comisión acumulada del año anterior
```

### 2. Fórmulas de Variación y Porcentajes de Crecimiento (YoY)
* **Desviación Porcentual del Monto Transaccionado:**
```dax
Fórmula DAX para el cálculo de porcentaje de variación del volumen transaccionado:
% VariacionTransacciones = DIVIDE(
        [TransaccionAñoActual],[TransaccionAñoAnterior], 0
    )
```

* **Desviación Porcentual del Monto Transaccionado con Check de Alerta Fraude:**
```dax
Fórmula DAX para el cálculo de porcentaje de variación del volumen transaccionado con check fraude:
%VariacionTotalFraude = 
VAR PorcentajeFila = 
DIVIDE(
        count(Transacciones[check_fraude]) - [CantCheckFraudeAñoAnterior], [CantCheckFraudeAñoAnterior]
    )

VAR PromedioFilasVisibles = 
    AVERAGEX(
        SUMMARIZE(
            Calendario, 
            Calendario[Month], 
            "@Porcentaje", DIVIDE(
        count(Transacciones[check_fraude]) - [CantCheckFraudeAñoAnterior], [CantCheckFraudeAñoAnterior]
    )
        ),
        [@Porcentaje]
    )

RETURN
    IF(
        ISINSCOPE(Calendario[Month]), 
        PorcentajeFila, 
        PromedioFilasVisibles
    )
```


* **Tasa de Crecimiento Anual de Comisiones (KPI Principal):**
```dax
Fórmula DAX que determina el crecimiento porcentual de comisiones YoY:
CAGR = 
    IF(
       [TotalComisionAñoAnterior] > 0, 
        (sum(Transacciones[comision]) / [TotalComisionAñoAnterior]) ^ (1 / 2) - 1, 
        BLANK()
    )
```

* **Tasa de Crecimiento Mensual de Comisiones (KPI Principal):**
```dax
Fórmula DAX que determina el crecimiento porcentual de comisiones MoM:
CrecimientoMoM = 
    DIVIDE(
        sum(Transacciones[comision]) - [TotalComisionAñoAnterior], 
        [TotalComisionAñoAnterior]
    )
```

### 3. Lógicas del Promedio y Desglose por Canal
* **Cálculo del Ticket Promedio Mensual:**
```dax
Fórmula DAX empleada para el promedio del monto transaccionado:
PromedioMontoAñoAnterior = CALCULATE(AVERAGE(Transacciones[monto]), SAMEPERIODLASTYEAR(Calendario[Date]))
```

* **Participación Proporcional del Método de Pago:**
```dax
Fórmula DAX que calcula el porcentaje de distribución por metodo de pago:
% Distribución Metodo = 
DIVIDE(
    Transacciones[monto], 
    CALCULATE(
        Transacciones[monto], 
        ALL(Metodo[Metodo_id])
    ),
    0
)
```
