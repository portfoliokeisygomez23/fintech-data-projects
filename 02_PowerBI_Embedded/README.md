# 📊 POWER BI Embedded - Capacity SKU A3 (Azure)

## 🚨 Problemática 
La solución que estaba operativa basada en licencias Power BI Pro presenta restricciones críticas:
* No permite escalar el uso de reportes embebidos
* Bloquea la generación de Embed Tokens
* Impide implementar soluciones orientadas a clientes (embedding)


## 🎯 Objetivo
Activación del servicio de PowerBI Embedded basada en la nube que permite:
* Consumo de los reportes desde la App Payku sin necesidad de licencias individuales de Power BI Pro.
* Garantizar seguridad de acceso a la información mediante RLS.
* Optimizar costos mediante capacidad dedicada (SKU A3).
* Generación de tokens de seguridad desde la Api Rest ilimitados.


## ✅ Solución Implementada
Adquirir una capacidad dedicada Power BI Embedded A3 a través de Microsoft Azure, lo que permitirá:
*	✔ Generación ilimitada de Embed Tokens
*	✔ Uso de Service Principal para autenticación
*	✔ Integración de reportes en aplicaciones web o sistemas internos
*	✔ Escalabilidad según demanda


## ✅ Arquitectura Implementada

![Arquitectura](../Imagenes/Arquitectura_Solucion.jpg)


## 🚀 Resultados
*	Habilitación de reportes en la APP Payku Usuarios
*	Mejora en la entrega de información a clientes
*	Base tecnológica para productos data-driven
* La solución permite a usuarios de negocio visualizar su información, cumpliendo con estándares de seguridad mediante Row-Level Security (RLS).
Actualmente, los reportes se encuentran en producción, operativa y consumida a través de APIs REST.


## 💡 BENEFICIOS OBTENIDOS
* Visualización integrada sin salir de la aplicación.
*	Reducción de dependencia de herramientas externas.
*	Mayor control de seguridad y acceso a datos.
*	Escalabilidad mediante capacidad dedicada.
*	Experiencia de usuario fluida y centralizada.


## 🛠️ Tecnologías Utilizadas
* Microsoft Power BI
* Microsoft PowerBI Embedded
* Azure Microsoft Entra ID

