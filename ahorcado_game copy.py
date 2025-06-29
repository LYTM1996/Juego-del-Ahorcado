import random
# Mostrar mensaje de bienvenida
print("<=== JUEGO DEL AHORCADO ===>")

def menu_principal ():
    print("\n== MENÚ PRINCIPAL ==")
    print("1. Jugar")
    print("2. Reglas del juego")
    print("3. Salir del Juego")
    return input("Selecciona una opción: ")

def jugar():
    print("\n--- MENÚ DE JUEGO ---")
    print("1. Un solo jugador")
    print("2. Contra la computadora")
    print("3. Multijugador (2 jugadores)")
    print("4. Ver estadísticas de la partida")
    print("5. Volver al menú principal")
    return input("Selecciona una opción: ")

def reglas_del_juego():
    print("\n--- REGLAS DEL JUEGO ---")
    print("1. Reglas del juego: un solo jugador")
    print("2. Reglas del juego: contra la computadora")
    print("3. Reglas del juego: multijugador (2 jugadores)")
    print("4. Volver al menú principal")
    return input("Selecciona una opción: ")

def salir_del_juego():
    print("\nSaliendo del juego. Gracias por jugar.")

def ver_reglas_juego_un_solo_jugador():
    print("\n --- REGLAS DEL JUEGO: UN SOLO JUGADOR ---")
    print("- Ingresar el nombre del jugador")
    print("- Decidir el número de partidas que se desea jugar")
    print("- La computadora escojerá una palabra al azar de una lista de palabras")
    print("- La computadora le pedirá al jugador ingresar una letra")
    print("- Si la letra pertenece a la palabra secreta, el sistema mostrará la palabra adivinada hasta el momento así (_ _ a _ _).:")  
    print("- Si no está, se le resta una vida al jugador.")
    print("- El jugador tiene 6 vidas.")
    print("- Si adivina toda la palabra antes de quedarse sin vidas, gana.")
    print("- Si se le terminan las vidas sin completar la palabra, pierde.")
    print("- Las letras repetidas no restan vidas si ya las adivinó antes.\n")
    return input("Presiona 4 para volver al REGLAS DEL JUEGO: ")

def ver_reglas_contra_la_computadora():
    print("\n --- REGLAS DEL JUEGO:  CONTRA LA COMPUTADORA ---")
    print("- Ingresar el nombre del jugador")
    print("- Decidir el número de partidas que se desea jugar")
    print("- Tú serás quien piense una palabra secreta (sin que la computadora la conozca).")
    print("- La computadora intentará adivinar la palabra, preguntando una letra a la vez.")
    print("- Tú deberás responder si la letra está o no en la palabra:")
    print("- Si la letra está, el sistema mostrará la palabra adivinada hasta el momento (_ _ a _ _).")  
    print("- Si no está, se le resta una vida a la computadora.")
    print("- La computadora tiene 6 vidas.")
    print("- Si adivina toda la palabra antes de quedarse sin vidas, gana.")
    print("- Si se le terminan las vidas sin completar la palabra, pierde.")
    print("- Las letras repetidas no restan vidas si ya las adivinó antes.\n")
    return input("Presiona 4 para volver al REGLAS DEL JUEGO: ")

def ver_reglas_juego_multijugador():
    print("\n --- REGLAS DEL JUEGO:  MULTIJUGADOR (2 JUGADORES) ---")
    print("- Ingresar el nombre del jugador 1 y el nombre del jugador 2")
    print("- Decidir el número de partidas que se desea jugar")
    print("- El Jugador 1 ingresa una palabra secreta (el otro jugador no debe verla).")
    print("- El Jugador 2 intentará adivinar la palabra letra por letra.")
    print("- El sistema mostrará la palabra como espacios vacíos (_ _ _ _).")
    print("- Si la letra ingresada está en la palabra, se revela en su posición.")
    print("- Si no está, se pierde una vida.")
    print("- Hay 6 vidas disponibles para el Jugador que adivine.")
    print("- No se penaliza por repetir letras ya usadas.")
    print("- El juego termina cuando el Jugador 2 adivina toda la palabra o se queda sin vidas.\n")
    return input("Presiona 4 para volver al REGLAS DEL JUEGO: ")

def solicitar_nombres(modo):
    nombres = {}
    if modo == "1":
        nombres["jugador1"] = input("Ingrese su nombre: ").strip()
    elif modo == "2":
        nombres["jugador1"] = input("Ingrese su nombre: ").strip()
        nombres["computadora"] = "Computadora"
    elif modo == "3":
        nombres["jugador1"] = input("Nombre del Jugador 1 (define la palabra): ").strip()
        nombres["jugador2"] = input("Nombre del Jugador 2 (adivina la palabra): ").strip()
    return nombres

def jugar_un_solo_jugador():
    # Lista de palabras ocultas posibles
    palabras = ["inflamable", "antiguo", "programacion", "suculenta", "inmigrante", "aleatorio", "tecnologia", "cuchillo", "gimnasio", "lisbeh"]
    # Elegir una palabra al azar
    palabra = random.choice(palabras)
    # Número de intentos permitidos
    vidas = 6

    # Guardar las letras que el jugador adivina
    letras = []
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

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            while True:
                sub_opcion = jugar()
                if sub_opcion == "1":
                    print("\n--- JUGANDO: UN SOLO JUGADOR ---")
                    jugar_un_solo_jugador()
                    # llamando a la función del juego para un solo jugador
                elif sub_opcion == "2":
                    print("\n--- JUGANDO: CONTRA LA COMPUTADORA ---")
                    # llamando a la función del juego contra la computadora
                elif sub_opcion == "3":
                    print("\n--- JUGANDO: MULTIJUGADOR (2 JUGADORES) ---")
                    # llamando a la función del juego para 2 jugadores
                elif sub_opcion == "4":
                    print("\n--- MOSTRANDO ESTADÍSTICAS DE LA PARTIDA ---")
                    # Aquí se mostrarían las estadísticas de la partida
                elif sub_opcion == "5":
                    break
        elif opcion == "2":
            while True:
                sub_opcion = reglas_del_juego()
                if sub_opcion == "1":
                    while True:
                        opcion_reglas = ver_reglas_juego_un_solo_jugador()
                        if opcion_reglas == "4":
                            break
                elif sub_opcion == "2":
                    while True:
                        opcion_reglas = ver_reglas_contra_la_computadora()
                        if opcion_reglas == "4":
                            break
                elif sub_opcion == "3":
                    while True:
                        opcion_reglas = ver_reglas_juego_multijugador()
                        if opcion_reglas == "4":
                            break 
                elif sub_opcion == "4":
                    break
        elif opcion == "3":
            salir_del_juego()
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

main()