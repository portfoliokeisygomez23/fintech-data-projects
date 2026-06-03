# 🌐 Arquitectura de Analítica Embebida: Integración con Power BI Embedded

## 📝 Resumen del Proyecto
Diseño e implementación de una arquitectura de analítica embebida de nivel empresarial para integrar tableros de control directamente en el portal web de la empresa (Frontend en **React**). La solución transforma reportes internos en un producto analítico orientado al cliente final (*Customer-Facing Analytics*), utilizando la **API REST de Power BI** para una carga fluida y garantizando un aislamiento estricto de los datos mediante un modelo multi-inquilino (*Multi-tenancy*).

---

## 🎯 El Reto
El desafío principal consistía en disponibilizar tableros analíticos a miles de usuarios externos sin requerir que cada uno contara con una licencia de Power BI, manteniendo el rendimiento de las consultas y asegurando que ningún cliente pudiera visualizar información de otro (Gobernanza y Seguridad).

---

## 🏗️ Arquitectura Técnica del Ecosistema

La solución se estructuró dividiendo las responsabilidades en capas claras dentro de Power BI Service y el backend de la aplicación:

### 1. Capa de Contenedores: Workspace Dedicado
* **Creación de Workspace** 
* **Tipo de Capacidad:** Alojado en una capacidad dedicada de Azure (**Power BI Embedded Capacidad A3-Sku**) para permitir el consumo ilimitado de usuarios anonimizados mediante el esquema *App Owns Data* (La aplicación posee los datos).
* **Aislamiento:** Este espacio de trabajo está aislado de la reportería interna de la empresa, conteniendo exclusivamente los artefactos que serán expuestos al exterior.

### 2. Capa de Datos: Modelo Semántico Dinámico (Dataset)
* **Modo de Almacenamiento:** Configurado en **Import Mode** con actualizaciones programadas diarias cada 3 horas, para optimizar costos de procesamiento.
* **Centralización:** Un único modelo semántico atiende a todos los clientes de la plataforma. Se consolidaron las tablas de hechos y dimensiones bajo un **Esquema en Estrella** altamente indexado.
* **Parámetro Clave (`Cliente ID`):** Se definió un parámetro global de tipo texto dentro del modelo, el cual actúa como el puente de comunicación con la API de la aplicación para filtrar el contexto del usuario logueado.

### 2. Capa de Datos: Modelo Semántico Dinámico (Dataset)

* **Modelos Semánticos:** Se vincularon de forma nativa los **4 modelos semánticos independientes** (segmentados por Negocio/Pais), garantizando que la lógica de cálculo ya estuviera optimizada antes de la fase de integración web.

> 💡 **Nota de Diseño:** Al reutilizar los 4 modelos existentes en lugar de duplicar la data, se logró mantener una **única fuente de verdad** y se redujo a cero el esfuerzo de mantenimiento del backend de datos durante el despliegue del entorno embebido.
> 

### 3. Capa de Visualización: Reportes Core
* **Diseño UX/UI:** Desarrollado con páginas de estilo personalizadas para homologar los colores, tipografías y componentes visuales con la paleta de la aplicación web, logrando que el reporte se perciba como una sección nativa del software.
* **Navegación:** Se deshabilitaron las barras de navegación nativas de Power BI, delegando los filtros y el cambio de pestañas a botones personalizados embebidos en el frontend.

---

## 🔐 Arquitectura de Seguridad y Flujo de Autenticación (RLS Dinámico)

Para garantizar la confidencialidad de la información en un entorno multi-inquilino, el flujo de acceso sigue una arquitectura síncrona basada en **Row-Level Security (RLS)** controlado por el backend.

Dentro del modelo semántico se configuró un rol de seguridad activa por medio de un parámetro llamado `RLS`. Este aplica un filtro dinámico sobre la tabla de Clientes mediante la siguiente expresión DAX:

[Clientes.cliente_id] = CONTAINSSTRING(CUSTOMDATA(),Clientes[cliente_id])

> ℹ️ Nota técnica: Al utilizar el esquema de Power BI Embedded, el valor devuelto por la función USERNAME() no corresponde a un correo electrónico de Azure AD, sino al string alfanumérico estricto del cucu_identificador que la API REST del backend inyecta dinámicamente al momento de generar el Embed Token.
>

---

## 💡 Impacto y Beneficios Obtenidos

* 💰 **Monetización de Datos:** El ecosistema permitió lanzar un nuevo módulo "Premium" de analítica avanzada dentro de la plataforma web, abriendo una línea de ingresos adicional e incremental para la compañía.

* 📉 **Eficiencia en Costos:** Al implementar la arquitectura App Owns Data, la organización evita la adquisición de licencias individuales (Power BI Pro) para miles de usuarios externos, pagando únicamente por los recursos de la capacidad encendida en Azure.

* 🛡️ **Seguridad Certificada:** Mitigación total del riesgo de filtración de información (Data Leakage) entre cuentas. Al ejecutarse la seguridad directamente en el motor de Power BI (Backend), las reglas de acceso son inviolables y no pueden ser manipuladas desde las herramientas de desarrollador en el navegador del cliente (Frontend).

---

## 🛠️ Stack Tecnológico Utilizado

* ✔ **BI Core:** Power BI Desktop / Power BI Service (Embedded Capacity A3-Sku).

* ✔ **Backend Integration:** API REST de Power BI, Azure Active Directory (Service Principal / OAuth 2.0).

* ✔ **Frontend Component:** Power BI Client React Library (powerbi-client-react).








## 📝 Resumen del Proyecto


---

## 🎯 El Reto


---

## 🛠️ Solución Implementada

### 1. Análisis y Extracción
* **Auditoría de Datos:** Análisis profundo de la base de datos origen para entender la lógica de negocio y la calidad de la información.
* **Limpieza (Data Cleansing):** Estandarización de tipos de datos, tratamiento de nulos y normalización de registros mediante Power Query.
* **Infraestructura de Conectividad:** Configuración y administración de un **On-premises Data Gateway** instalado en un **servidor dedicado** exclusivamente para garantizar la comunicación segura entre el entorno local y Power BI Service.

---

### 2. Arquitectura y Modelado
* **Diseño de la Arquitectura de Datos:** Implementación de un flujo híbrido que conecta la base de datos MySQL local con la nube de Power BI a través de un Gateway en un servidor dedicado.

![Arquitectura](../Imagenes/Arquitectura.jpg)
* **Diseño de Modelo en Estrella:** Creación de un **Modelo Semántico** eficiente separando Tablas de Hechos (Facts) y Dimensiones (Dims).

![Modelo Estrella](../Imagenes/Entidad_Relacion_Completo.jpg)
* **Optimización de Recursos:** Implementación de **Live Connection** para permitir que múltiples reportes consuman el mismo modelo. Esto garantiza la consistencia de las métricas (Única Fuente de Verdad) y reduce drásticamente el uso de almacenamiento y memoria.
* **Integridad Referencial:** Establecimiento de relaciones (Joins) respetando estrictamente las reglas del negocio para evitar duplicidad o pérdida de información.

---

### 3. Optimización de Carga: Actualización Incremental
Dada la naturaleza transaccional del negocio Fintech, implementé una estrategia de **Incremental Refresh** para maximizar el rendimiento:
* **Configuración de Parámetros:** Uso de `RangeStart` y `RangeEnd` para segmentar la ingesta de datos.
* **Eficiencia de Recursos:** Reducción del tiempo de refresco al procesar solo los datos nuevos, minimizando el impacto en el servidor MySQL origen ni excediendo los límites de memoria de Power BI Service.

---

### 4. Distribución y Democratización de Datos
Para maximizar el valor del modelo semántico centralizado, se desplegó un ecosistema de visualización de alto impacto:
* **Ecosistema de Reportes:** Creación de **30 dashboards especializados** que consumen el modelo único vía *Live Connection*, asegurando que todas las áreas consulten la misma información.
* **Alcance Departamental:** Implementación de soluciones analíticas a medida para:
    * **Compliance:** Monitoreo de riesgos y cumplimiento normativo.
    * **Atención al Cliente:** KPIs de servicio, tiempos de respuesta y satisfacción.
    * **RRHH:** Gestión de talento y métricas operativas de personal.
    * **Contabilidad & Gerencial:** Control financiero y visión estratégica de alto nivel.
    * **Operativos:** Seguimiento de procesos core en tiempo real.

![Reporte1](../Imagenes/Reporte4.jpg)

![Reporte2](../Imagenes/Reporte5.jpg)

---

## 5. 📊 Componentes Técnicos
* **Base de Datos:** MySQL (On-Premises)
* **Conectividad:** Data Gateway en Servidor Dedicado
* **Modelado:** Esquema en Estrella (Star Schema)
* **Herramientas:** Power BI Desktop, DAX, Power Query
* **Automatización:** Actualización Incremental (Schedule diario)

---

## 6. 💡 Impacto en el Negocio
* **Eficiencia Operativa:** Reducción del **100% en el tiempo manual** de preparación de reportes mediante la automatización de la ingesta y el modelado.
* **Escalabilidad:** Diseño lógico (Modelo Estrella) preparado para absorber un incremento volumétrico sin necesidad de reestructurar la lógica de negocio.
* **Confianza & Calidad:** Consolidación de una "Única Fuente de Verdad", eliminando discrepancias de datos en un **20%** entre departamentos.
* **Optimización de Carga:** Gracias a la actualización incremental, el tiempo de procesamiento en el servidor disminuyó en un **60%**, evitando bloqueos en la base de datos transaccional.

---

## 7. ⚠️ Desafíos y Diagnóstico Técnico
Actualmente, la arquitectura ha identificado puntos críticos de mejora debido al crecimiento de los datos:
* **Cuellos de Botella:** El servidor dedicado al Gateway está experimentando saturación durante los procesos de actualización, lo que limita la velocidad de disponibilidad de la información.

---

## 8. 🚀 Próximos Pasos (RoadMap)
Como estrategia de optimización y escalabilidad, se ha definido:
* **Migración a la Nube:** Evolucionar la arquitectura hacia **Google Cloud Platform (GCP)** para eliminar la dependencia de servidores físicos, suprimir los cuellos de botella del Gateway y mejorar la alta disponibilidad del ecosistema analítico.

