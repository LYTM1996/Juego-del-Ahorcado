import random
import getpass

# Estadísticas globales
estadisticas = {
    "total_partidas": 0,
    "un_jugador": {"ganadas": 0, "perdidas": 0},
    "contra_computadora": {"jugador": {"ganadas": 0, "perdidas": 0}, "computadora": {"ganadas": 0, "perdidas": 0}},
    "multijugador": {"jugador1": {"ganadas": 0, "perdidas": 0}, "jugador2": {"ganadas": 0, "perdidas": 0}},
    "resumen_partidas": []  # Lista para registrar los resultados de cada partida
}

def mostrar_estadisticas_modo(modo):    
    if modo == "un_jugador":
        print(f"\n--- Estadísticas del modo {modo.replace('_', ' ')} ---")
        data = estadisticas[modo]
        print(f"Ganadas: {data['ganadas']}")
        print(f"Perdidas: {data['perdidas']}")
    elif modo == "contra_computadora":
        print(f"\n--- Estadísticas del modo {modo.replace('_', ' ')} ---")
        j = estadisticas[modo]["jugador"]
        c = estadisticas[modo]["computadora"]
        print(f"Jugador: Ganadas: {j['ganadas']}, Perdidas: {j['perdidas']}")
        print(f"Computadora: Ganadas: {c['ganadas']}, Perdidas: {c['perdidas']}")
    elif modo == "multijugador":
        print(f"\n--- Estadísticas del modo {modo.replace('_', ' ')} ---")
        j1 = estadisticas[modo]["jugador1"]
        j2 = estadisticas[modo]["jugador2"]
        print(f"Jugador 1: Ganadas: {j1['ganadas']}, Perdidas: {j1['perdidas']}")
        print(f"Jugador 2: Ganadas: {j2['ganadas']}, Perdidas: {j2['perdidas']}")
    elif modo == "partidas":
        # Verificar si todas las estadísticas están en cero
        if (
            estadisticas['total_partidas'] == 0 and
            estadisticas['un_jugador']['ganadas'] == 0 and estadisticas['un_jugador']['perdidas'] == 0 and
            estadisticas['contra_computadora']['jugador']['ganadas'] == 0 and estadisticas['contra_computadora']['jugador']['perdidas'] == 0 and
            estadisticas['contra_computadora']['computadora']['ganadas'] == 0 and estadisticas['contra_computadora']['computadora']['perdidas'] == 0 and
            estadisticas['multijugador']['jugador1']['ganadas'] == 0 and estadisticas['multijugador']['jugador1']['perdidas'] == 0 and
            estadisticas['multijugador']['jugador2']['ganadas'] == 0 and estadisticas['multijugador']['jugador2']['perdidas'] == 0
        ):
            print("\nNo hay estadísticas recientemente.")
            return

        print("\n--- ESTADÍSTICAS FINALES ---")
        print(f"Total de partidas jugadas: {estadisticas['total_partidas']}")
        
        print("\nResumen de cada partida:")
        for i, resumen in enumerate(estadisticas["resumen_partidas"], start=1):
            print(f"{i}. {resumen}")
        
        print("\nEstadísticas por modo de juego:")
        
        print("\n- Un solo jugador:")
        print(f"  Ganadas: {estadisticas['un_jugador']['ganadas']}")
        print(f"  Perdidas: {estadisticas['un_jugador']['perdidas']}")
        
        print("\n- Contra la computadora:")
        print(f"  Jugador 1: Ganadas: {estadisticas['contra_computadora']['jugador']['ganadas']}, Perdidas: {estadisticas['contra_computadora']['jugador']['perdidas']}")
        print(f"  Computadora: Ganadas: {estadisticas['contra_computadora']['computadora']['ganadas']}, Perdidas: {estadisticas['contra_computadora']['computadora']['perdidas']}")
        
        print("\n- Multijugador:")
        print(f"  Jugador 1: Ganadas: {estadisticas['multijugador']['jugador1']['ganadas']}, Perdidas: {estadisticas['multijugador']['jugador1']['perdidas']}")
        print(f"  Jugador 2: Ganadas: {estadisticas['multijugador']['jugador2']['ganadas']}, Perdidas: {estadisticas['multijugador']['jugador2']['perdidas']}")

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
    print("4. Ver estadísticas de la última partida")
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
    if modo == "1": # Un solo jugador
        nombre_1 = input("Ingrese su nombre: ")
        return nombre_1, None
    elif modo == "2": # Contra la computadora
        nombre_1 = input("Ingrese su nombre: ")
        return nombre_1, "Computadora"
    elif modo == "3": # Multijugador (2 jugadores)
        nombre_1 = input("Nombre del Jugador 1: ")
        nombre_2 = input("Nombre del Jugador 2: ")
        return nombre_1, nombre_2
    else:
        return None, None

def mostrar_palabra_con_letras_adivinadas(palabra, letras):
    mostrada = ""
    for l in palabra:
        if l in letras:
            mostrada += l + " "
        else:
            mostrada += "_ "
    return mostrada


# ======================== SE DECLARA LA FUNCIÓN UN SOLO JUGADOR ========================
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
        mostrada = mostrar_palabra_con_letras_adivinadas(palabra, letras)
        print("\n", mostrada)
        # Verificar si ya adivinó todo
        if "_" not in mostrada: 
            print("Ganaste")
            estadisticas["un_jugador"]["ganadas"] += 1
            estadisticas["total_partidas"] += 1
            break
    # Si pierde
    if vidas == 0:
        print("Perdiste. La palabra era:", palabra)
        estadisticas["un_jugador"]["perdidas"] += 1
        estadisticas["total_partidas"] += 1
# ======================== SE DECLARA LA FUNCIÓN JUGAR CONTRA LA COMPUTADORA ========================
def jugar_contra_la_computadora():
    # Solicitar al jugador 1 que ingrese una palabra secreta
    palabra = input("Ingresa una palabra secreta (la computadora intentará adivinarla): ").lower()
    vidas_computadora = 6
    intentos_computadora = []
    # Mostrar espacios vacíos
    print("_ " * len(palabra))

    while vidas_computadora > 0:
        letra_computadora = random.choice("abcdefghijklmnopqrstuvwxyz")
                
        # Validar que la letra no haya sido adivinada antes
        if letra_computadora in intentos_computadora:
            continue

        intentos_computadora.append(letra_computadora)
        
        validar_letra = input("La letra (- " + letra_computadora + " -) está en la palabra? (Si/No): ").strip().lower()

        if validar_letra == "si":
            print("¡Acertaste! La letra forma parte de la palabra")
        else:
            vidas_computadora -= 1
            print("La letra no está en la palabra. Vidas restantes de la computadora:", vidas_computadora)
        # Mostrar la palabra con las letras adivinadas
        mostrada = mostrar_palabra_con_letras_adivinadas(palabra, intentos_computadora)
        print("\n", mostrada)
        # Verificar si la computadora adivinó toda la palabra
        if "_" not in mostrada: 
            print("La computadora ganó.")
            estadisticas["contra_computadora"]["jugador"]["perdidas"] += 1
            estadisticas["contra_computadora"]["computadora"]["ganadas"] += 1
            estadisticas["total_partidas"] += 1
            break

    if vidas_computadora == 0:
        print("Computadora perdió. La palabra era:", palabra)
        estadisticas["contra_computadora"]["jugador"]["ganadas"] += 1
        estadisticas["contra_computadora"]["computadora"]["perdidas"] += 1
        estadisticas["total_partidas"] += 1

# ======================== SE DECLARA LA FUNCIÓN JUGAR MULTIJUGADOR ========================
def jugar_multijugador():
    # Solicitar al jugador 1 que ingrese una palabra secreta
    print("\n**********************************************************************************************************")
    palabra = getpass.getpass("\nJugador 1: ingrese una palabra secreta (el jugador 2 intentará adivinarla): ").lower()
    
    vidas_jugador_2 = 6
    intentos_jugador_2 = []
    # Mostrar espacios vacíos
    print("_ " * len(palabra))

    while vidas_jugador_2 > 0:
        letra_jugador_2 = input("Jugador 2: ingrese una letra: ")
                
         # Validar que la entrada sea una letra
        if not letra_jugador_2.isalpha():
            print ("*** Entrada no válida. Usa únicamente letras ***")
            continue

        # Verificar que solo ingrese una letra
        if len(letra_jugador_2) != 1:
            print("*** La entrada no es válida. Solo se permite una letra por intento ***")
            continue

        # Verificar si ya la escribió antes
        if letra_jugador_2 in intentos_jugador_2:
            print("*** Esa letra ya fue ingresada. Prueba con otra. ***")
            continue

        intentos_jugador_2.append(letra_jugador_2)
        
        validar_letra = input("Jugador 1: La letra (- " + letra_jugador_2 + " -) está en la palabra? (Si/No): ").strip().lower()

        if validar_letra == "si":
            print("¡Acertaste! La letra forma parte de la palabra")
        elif validar_letra == "no":
            vidas_jugador_2 -= 1
            print("Esa letra no está en la palabra. Jugador 2 tiene ",vidas_jugador_2," vidas restantes")
        else:
            print("*** Respuesta no válida. Por favor, responde con 'Si' o 'No'. ***")
        # Mostrar la palabra con las letras adivinadas
        mostrada = mostrar_palabra_con_letras_adivinadas(palabra, intentos_jugador_2)
        print("\n", mostrada)
        # Verificar si la computadora adivinó toda la palabra
        if "_" not in mostrada: 
            print("Jugador 2 ha ganado")
            estadisticas["multijugador"]["jugador1"]["perdidas"] += 1
            estadisticas["multijugador"]["jugador2"]["ganadas"] += 1
            estadisticas["total_partidas"] += 1
            break

    if vidas_jugador_2 == 0:
        print("Jugador 2 perdió. La palabra era:", palabra)
        estadisticas["multijugador"]["jugador1"]["ganadas"] += 1
        estadisticas["multijugador"]["jugador2"]["perdidas"] += 1
        estadisticas["total_partidas"] += 1
# ======================== SE DECLARA LA FUNCIÓN PRINCIPAL ========================
def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            while True:
                sub_opcion = jugar()
                if sub_opcion == "1":
                    print("\n--- JUGANDO: UN SOLO JUGADOR ---")
                    nombres = solicitar_nombres(sub_opcion)
                    print(f"Jugador 1: {nombres[0]}")
                    respuesta = input("¿Deseas definir un número de partidas a jugar? (Si/No): ").strip().lower()
                    if respuesta == "si":
                        num_partidas = int(input("¿Cuántas partidas deseas jugar?: "))
                        for i in range(num_partidas):
                            print(f"\nPartida {i+1} de {num_partidas}")
                            jugar_un_solo_jugador()
                        mostrar_estadisticas_modo("un_jugador")
                    else:
                        while True:
                            jugar_un_solo_jugador()
                            mostrar_estadisticas_modo("un_jugador")
                            jugar_otra = input("¿Deseas jugar nuevamente? (Si/No): ").strip().lower()
                            if jugar_otra != "si":
                                break
                    # llamando a la función del juego para un solo jugador
                elif sub_opcion == "2":
                    print("\n--- JUGANDO: CONTRA LA COMPUTADORA ---")
                    nombres = solicitar_nombres(sub_opcion)
                    print(f"Jugador 1: {nombres[0]}")
                    print(f"Jugador 2: {nombres[1]}")
                    respuesta = input("¿Deseas definir un número de partidas a jugar? (Si/No): ").strip().lower()
                    if respuesta == "si":
                        num_partidas = int(input("¿Cuántas partidas deseas jugar?: "))
                        for i in range(num_partidas):
                            print(f"\nPartida {i+1} de {num_partidas}")
                            jugar_contra_la_computadora()
                        mostrar_estadisticas_modo("contra_computadora")
                    else:
                        while True:
                            jugar_contra_la_computadora()
                            mostrar_estadisticas_modo("contra_computadora")
                            jugar_otra = input("¿Deseas jugar nuevamente? (Si/No): ").strip().lower()
                            if jugar_otra != "si":
                                break
                    # llamando a la función del juego contra la computadora
                elif sub_opcion == "3":
                    print("\n--- JUGANDO: MULTIJUGADOR (2 JUGADORES) ---")
                    nombres = solicitar_nombres(sub_opcion)
                    print(f"Jugador 1: {nombres[0]}")
                    print(f"Jugador 2: {nombres[1]}")
                    respuesta = input("¿Deseas definir un número de partidas a jugar? (Si/No): ").strip().lower()
                    if respuesta == "si":
                        num_partidas = int(input("¿Cuántas partidas deseas jugar?: "))
                        for i in range(num_partidas):
                            print(f"\nPartida {i+1} de {num_partidas}")
                            jugar_multijugador()
                        mostrar_estadisticas_modo("multijugador")
                    else:
                        while True:
                            jugar_multijugador()
                            mostrar_estadisticas_modo("multijugador")
                            jugar_otra = input("¿Deseas jugar nuevamente? (Si/No): ").strip().lower()
                            if jugar_otra != "si":
                                break
                    # llamando a la función del juego para 2 jugadores
                elif sub_opcion == "4":
                    print("\n--- MOSTRANDO ESTADÍSTICAS ÚLTIMA PARTIDA ---")
                    mostrar_estadisticas_modo("partidas")
                    # Aquí se mostrarían las estadísticas de la partida
                elif sub_opcion == "5":
                    # Reiniciar estadísticas
                    estadisticas["total_partidas"] = 0
                    estadisticas["un_jugador"] = {"ganadas": 0, "perdidas": 0}
                    estadisticas["contra_computadora"] = {
                        "jugador": {"ganadas": 0, "perdidas": 0},
                        "computadora": {"ganadas": 0, "perdidas": 0}
                    }
                    estadisticas["multijugador"] = {
                        "jugador1": {"ganadas": 0, "perdidas": 0},
                        "jugador2": {"ganadas": 0, "perdidas": 0}
                    }
                    estadisticas["resumen_partidas"] = []
                    print("¡Estadísticas reiniciadas!")
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