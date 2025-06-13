import random

# Lista de palabras posibles
palabras = ["python", "ecuador", "programacion", "tecnologia", "computadora"]

# Elegir una palabra al azar
palabra = random.choice(palabras)

# Guardar las letras que el jugador adivina
letras = []

# Número de intentos permitidos
vidas = 6

# Mostrar mensaje de bienvenida
print("Juego del ahorcado")
print("_ " * len(palabra))  # Mostrar espacios vacíos

# Bucle del juego
while vidas > 0:
    letra_ingresada = input("Escribe una letra: ").lower()

    # Verificar que solo ingrese una letra
    if len(letra_ingresada) != 1:
        print("Solo una letra por favor.")
        continue

    # Verificar si ya la escribió antes
    if letra_ingresada in letras:
        print("Ya escribiste esa letra.")
        continue

    letras.append(letra_ingresada)

    # Revisar si la letra está en la palabra
    if letra_ingresada in palabra:
        print("¡Sí está!")
    else:
        vidas -= 1
        print("No está. Te quedan", vidas, "vidas")

    # Mostrar la palabra con las letras adivinadas
    mostrada = ""
    for l in palabra:
        if l in letras:
            mostrada += l + " "
        else:
            mostrada += "_ "

    print(mostrada)

    # Verificar si ya adivinó todo
    if "_" not in mostrada:
        print("¡Ganaste!")
        break

# Si pierde
if vidas == 0:
    print("Perdiste. La palabra era:", palabra)