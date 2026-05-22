# Side3 Project - Juego en Pygame

Un juego 2D desarrollado con Pygame donde controlas un personaje que puede moverse, rotar hacia el mouse y disparar balas.

## Requisitos

Este proyecto utiliza un entorno vitual para su desarrollo, por lo que antes de poder utulizarlo revisa bien que las dependencias estén instaladas en tu equipo. Recuerda que no es obligatorio utilizar un entorno virtual para poder hacer uso de este proyecto, pero es recomendable hacerlo.

- Python 3.13
- Pygame 2.6
- VENV (virtual environment)
- PIP

Puedes instalar las dependencias utilizando la siguiente instruccion: 
`pip install -requirements.txt` 

## Estructura del proyecto
El proyecto tiene tres capas principales:
- Raiz: Aqui es donde está el archivo main, utils y config.
- Characters: Aquí es donde existe todo lo relacionado a personajes que actuan directamente con el curso de gameplay del juego, tales como el propio jugador o enemigos varios.
- general OBjects: aquí se coloca todo lo relacionado a objetos que no se considern primordiales para el ciclo de gameplay, tales como proyecticles, objetos estaticos, etc.
- Resources: Al ser un proyecto pequeño se puede utilizar una carpeta exlusiva para poder alamecnar los distintos archivos visuales que se van a utilizar en el proyecto.
