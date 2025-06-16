import random

# Lista de palabras ocultas posibles
palabras = ["inflamable", "antiguo", "programacion", "suculenta", "inmigrante", "aleatorio", "tecnologia", "cuchillo", "gimnasio", "lisbeh"]
# Elegir una palabra al azar
palabra = random.choice(palabras)

# Número de intentos permitidos
vidas = 6

# Guardar las letras que el jugador adivina
letras = []

# Mostrar mensaje de bienvenida
print("Juego del ahorcado")
print("_ " * len(palabra))  # Mostrar espacios vacíos

# Bucle del juego
while vidas > 0:
    letra_ingresada = input("Escribe una letra: ").lower()

    # Validar que la entrada sea una letra
    if not letra_ingresada.isalpha():
        print ("Ingrese solo letras")
        continue

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
        print("Adivinaste, continúa")
    else:
        vidas -= 1
        print("Fallaste. Te quedan", vidas, "vidas")

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
        print("Ganaste")
        break

# Si pierde
if vidas == 0:
    print("Perdiste. La palabra era:", palabra)