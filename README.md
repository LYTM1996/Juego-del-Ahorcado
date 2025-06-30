------------------------------------------------------------------------------------------------------
Juego del Ahorcado en Python
------------------------------------------------------------------------------------------------------

Autor: Lisbeth Tipan
Materia: Lógica de Programación - Primer Semestre
Descripción: Este programa cosiste en el desarrollo del juego del "Ahorcado" desarrollado en Python. Con modalidades de Un jugador, Jugar contra la computadora y Multijugador. En donde el/los jugadores deben adivinar una palabra secreta, que será elegida aleatoriamente de una lista de palabras en el modo Un Jugador y asignada por el otro jugador en las modalidades Contra la computadora y Multijugador. La palabra  deberá ser adivinarda letra por letra, antes de quedarse sin los 6 intentos que se tiene y perder.
En este repositorio se encontrará el diagrama de flujo y el código fuente.
------------------------------------------------------------------------------------------------------
Definiciones:
--DIAGRAMA DE FLUJO--
Es una representación gráfica que muestra los pasos o decisiones de un proceso. Usa símbolos como flechas, rectángulos y rombos para mostrar el orden lógico de ejecución de un programa.

--DICCIONARIO EN PYTHON--
Es una estructura de datos que guarda pares de clave y valor. Se usa para almacenar datos organizados de forma que podamos buscarlos rápidamente por su “nombre”.

--BUCLE FOR--
Sirve para repetir algo un número exacto de veces o para recorrer una lista o secuencia.

--MÓDULO RANDOM--
Es una librería de Python que permite generar valores aleatorios, como elegir una palabra sorpresa para el ahorcado.

--MÓDULO GETPASS--
Permite al usuario escribir sin que se muestre en pantalla (útil para el modo multijugador, cuando el otro jugador no debe ver la palabra secreta).

------------------------------------------------------------------------------------------------------
Características:

- Importación del módulo random y getpass.
- Asignación de 10 palabras posibles para adivinar.
- Ingreso de palabra de Jugador 1 oculta.
- Selección aleatoria de palabras.
- 6 intentos para adivinar la palabra.
- Validación de entrada (solo letras, una por vez y sin repetirlas).
- Muestra el progreso con letras adivinadas y espacios en blanco (_ _ _ _).
- Informa al jugador cuando gana o pierde, y las vidas que le quedan.
- Informa estadística y resultados que al salir del juego se borran.
------------------------------------------------------------------------------------------------------
Principales Funcionalidades:

--MENÚ PRINCIPAL--
Permite al usuario elegir entre:
- Jugar
- Ver las reglas del juego
- Salir del programa

--MODO DE JUEGO--
- **Un solo jugador:** El sistema elige una palabra aleatoria y el jugador intenta adivinarla.
- **Contra la computadora:** El jugador define la palabra, y la computadora intenta adivinarla con letras aleatorias.
- **Multijugador:** Jugador 1 define la palabra y Jugador 2 trata de adivinarla letra por letra.

--REGISTRO DE ESTADÍSTICAS--
- Lleva un conteo de:
  - Partidas ganadas y perdidas por modo de juego
  - Resultados individuales por jugador y por computadora
  - Número total de partidas jugadas
- Se puede visualizar un resumen al finalizar las partidas o desde el menú.

--REGLAS DEL JUEGO--
- Cada modo tiene su sección de reglas accesible desde el menú principal.
- Las reglas explican el número de vidas, penalizaciones y condiciones de victoria/derrota.

--CONTROL DE FLUJO--
- Los usuarios pueden definir cuántas partidas jugar o seguir jugando hasta que decidan detenerse.
- El flujo incluye validación de entradas y opciones para volver atrás.

------------------------------------------------------------------------------------------------------
Instrucciones de uso:

1. Asegúrate de tener Python instalado (versión 3 o superior).
2. Guarda el archivo con el código en un archivo llamado ahorcado_game.py.
3. Abre una terminal o consola de comandos.
4. Ejecuta el programa con el siguiente comando en la consola:

  python ahorcado_game.py 
  
5. En las opciones del Menú, selecionar ingresando el número de cada opción.
-------------------------------------------------------------------------------------------------------
--NOTAS FINALES--
Este proyecto es una excelente introducción a:
- La programación modular en Python
- El uso de estructuras de control (`while`, `for`, `if`)
- Interacción con el usuario por consola
- Manejo de diccionarios para estadísticas
- Se definen funciones para evitar redundancias en el código. 