# Avance del Proyecto – Semana 3

## Descripción General

En este avance se realizó la estructuración del repositorio del proyecto y el desarrollo del módulo Core del sistema de alarmas. El objetivo principal fue pasar de una idea teórica a un componente funcional que permita procesar información y tomar decisiones básicas.

---

## Estructura del Repositorio

El repositorio fue organizado de forma clara para facilitar el orden y el mantenimiento del proyecto. Se utilizaron las siguientes carpetas:

- src: contiene la lógica principal del sistema.
- tests: carpeta destinada a futuras pruebas del sistema.
- docs: almacena la documentación del proyecto.
- database: contiene archivos relacionados con la base de datos.

Además, se implementó un archivo .gitignore para evitar subir archivos innecesarios al repositorio.

---

## Desarrollo del Módulo Core

El módulo Core representa el corazón del sistema de alarmas. En este módulo se desarrolló una clase principal encargada de procesar los datos que recibe el sistema desde los sensores.

La función principal del módulo permite:
- Recibir información de un sensor.
- Validar que los datos no estén vacíos ni sean negativos.
- Analizar la información recibida.
- Activar una alerta cuando se detecta una situación anormal.

Este módulo fue desarrollado sin interfaz gráfica y sin conexión a una base de datos, cumpliendo con el requisito de ser un módulo puro enfocado únicamente en la lógica del negocio.

---

## Seguridad y Validación de Datos

Para mejorar la seguridad del sistema, se implementaron validaciones de entrada que evitan el procesamiento de datos incorrectos. Si el sistema recibe información vacía, negativa o incoherente, esta es rechazada y no se genera ninguna acción.

Estas validaciones ayudan a prevenir errores y aseguran que el sistema solo trabaje con información confiable.

---

## Conclusión

Con este avance se logró establecer una base sólida para el proyecto, demostrando un repositorio bien estructurado y un módulo Core funcional. Este componente permite que el sistema tome decisiones básicas y se encuentra listo para futuras mejoras.
