# Trabajo-Integrador-Programacion

Sistema de Gestión de Países en Python con arquitectura modular en 7 capas. Desarrollado para el Trabajo Practico Integrador de Programacion 1

**Descripción del Proyecto:**

Este sistema permite la gestión y el análisis de datos demográficos y geográficos de diferentes países del mundo.
A partir de un dataset inicial de fuentes confiables procesado en Excel, la aplicación realiza filtros personalizados, ordenamientos eficientes, búsquedas específicas y reportes estadísticos avanzados.


**Institución:** Universidad Tecnológica Nacional (UTN) - Facultad Regional San Nicolás

**Alumno:** Flores Gustavo Ariel

**Comisión:** M26 (C1-24 - 1er Cuatrimestre)

**Profesores:** Ariel Enferrel, Martín A. García, Cinthia Rigoni

**Tutor:** Guada Maricchiolo

**Estructura del Software (Arquitectura)**

**main.py:** Orquestador principal y control del menú interactivo.

**archivos.py:** Persistencia de datos (lectura y escritura en el CSV).

**busqueda.py:** Alta de países, actualización de registros y búsqueda por nombre.

**estadistica.py:** Cálculo de valores extremos (máximos y mínimos) y promedios generales.

**filtros.py:** Búsquedas personalizadas por continente, población o superficie.

**ordenamiento.py:** Reorganización dinámica de tablas (ascendente/descendente y alfabética).

**presentacion.py:** Capa visual experta en el formateo de tablas en consola.

**Cómo Ejecutar el Proyecto:**

1. Clonar el repositorio.
   
2. Asegurarse de tener el archivo `PAISES.csv` en la ruta correspondiente.
   
3. Ejecutar el archivo central desde la consola: