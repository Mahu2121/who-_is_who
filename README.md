# Who_is_Who

# Tabla de contenidos



- [Who\_is\_Who](#who_is_who)
- [Tabla de contenidos](#tabla-de-contenidos)
- [Introducción](#introducción)
- [Manual](#manual)
  - [Pre-requisitos](#pre-requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción técnica](#descripción-técnica)
  - [Requisitos funcionales/no funcionales, NOT LIST](#requisitos-funcionalesno-funcionales-not-list)
      - [Requisitos funcionales:](#requisitos-funcionales)
      - [Requisitos no funcionales:](#requisitos-no-funcionales)
      - [NOT LIST](#not-list)
  - [Historias de usuaria](#historias-de-usuaria)
  - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
- [Diseño](#diseño)
  - [Diagrama de Componentes](#diagrama-de-componentes)
- [Implementación](#implementación)
  - [Tecnologías y Herramientas utilizadas](#tecnologías-y-herramientas-utilizadas)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Pruebas](#pruebas)
  - [Coverage](#coverage)
  - [Test de unidad](#test-de-unidad)
  - [Test de integración](#test-de-integración)
- [Análisis del tiempo invertido](#análisis-del-tiempo-invertido)
  - [Clockify + Wakatime](#clockify--wakatime)
  - [Justificación temporal](#justificación-temporal)
- [Conclusiones](#conclusiones)
  - [Posibles mejoras](#posibles-mejoras)
  - [Dificultades](#dificultades)

# Introducción
  Who is Who es un proyecto hecho por [Pablo Pontanilla Moreira](https://github.com/Pontax02) y [Hugo González Besada](https://github.com/Mahu2121) para demostrar los conocimientos obtenidos en los primeros meses del ciclo de DAM(curso 2024-2025) en el IES de TEIS, el proyecto esta escrito en python usando el framework reflex para la interfaz web

# Manual


## Pre-requisitos
* Python 3.12
* El framework Reflex
* Las librerias random, pytest , unittest


## Instalación

1. <strong> Clona el repositorio de GitHub</strong>: git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

2. <strong> Iniciar o entorno virtual </strong> Ejecuta los siguientes comantos "python3 -m venv .venv" y source ".venv/bin/activate" 

3. <strong> Instalar reflex </strong>: Ejecuta el comando "pip install reflex" 



## Uso
1. Al iniciar la aplicación, se cargará la interfaz principal.

2. Hacer clic en el botón Empezar para seleccionar un personaje aleatorio.

3. Introducir preguntas relacionadas con las características físicas de los personajes.

4. Utilizar el cuadro de entrada para adivinar el personaje.

5. Seguir jugando hasta acertar o finalizar la partida.

# Metodología

La metodologia usada fue dividir el proyecto en historias de usuario y realizando tdd en python puro mientras que ibamos documentandonos sobre las posibilidades que ofrecia reflex

# Descripción técnica

La aplicación se basa en una arquitectura <u>modular</u>:

<strong>Backend</strong>: Proporciona la lógica para el filtrado y selección de personajes.

<strong>Frontend</strong>: Maneja la interacción del usuario y muestra los resultados.


## Requisitos funcionales/no funcionales, NOT LIST

#### Requisitos funcionales: 
* Permitir al usuario realizar preguntas sobre las características de los personajes.

* Filtrar personajes en base a las respuestas.

* Permitir adivinar el personaje seleccionado.


#### Requisitos no funcionales:

* Interfaz intuitiva y fácil de usar.

* Código modular para facilitar mantenibilidad.

#### NOT LIST

* IN SCOPE ->  Levantar tablero, hacer preguntas y adivinar personaje

* OUT OF SCOPE -> Tabla de Clasificaciones, quitar las cartas manualmente

* UNRESOLVED -> temática de decoracion

## Historias de usuaria

|**¿Quién?** | **¿Qué quiere hacer?** | **¿Para qué lo quiere hacer?** |
|:-:|:-:|:-:|
|  La Jugadora  |  Elegir una carta aleatoria  |  Para comenzar a jugar |
|  La Jugadora  |  Realizar preguntas  |  Para descartar personajes que no son el que eligió  |
|  La Jugadora  |  Adivinar  |  Para terminar la partida y ganar/perder  |


## Arquitectura de la aplicación

 Esta compuesta por tres entornos , Frontend , Backend y la App

  1- El frontend es el apartado visual que la usuaria ve en su pantalla (La vista)

  2- El backend es donde el controlador realiza los cambios a traves del modelo y actualiza la vista
  
  3- Es la interaccion entre el frontend y backend , donde los cambios detectados en el front pasan al backend

# Diseño

## Diagrama de Componentes

# Implementación

## Tecnologías y Herramientas utilizadas

## Backend

## Frontend

# Pruebas

## Coverage

## Test de unidad

## Test de integración

# Análisis del tiempo invertido

## Clockify + Wakatime

## Justificación temporal

# Conclusiones

## Posibles mejoras

Agregar más características a los personajes para aumentar la complejidad.

Implementar un sistema de puntuación.

Optimizar la interfaz 

## Dificultades

Es la primera vez que usamos un framework, en este caso "Reflex" lo que hizo que tuvieramos que aprender desde el principio como funciona y como integrar el backend al la interfaz. Tambien era la primera vez que veiamos las clases de estado que al final resultaron ser vitales para, por ejemplo ir cambiando el imput introducido por el usuario y guardarlo para comparar.