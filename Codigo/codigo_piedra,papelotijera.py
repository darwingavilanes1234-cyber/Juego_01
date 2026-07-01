import random

# =========================================
# JUEGO: PIEDRA, PAPEL O TIJERA
# Proyecto Integrador - Lógica de Programación
# Estudiante: Darwin Gavilanes Gavilanes
# =========================================

# Lista de opciones válidas
opciones = ["piedra", "papel", "tijera"]


def mostrar_bienvenida():
    """Muestra la información inicial del juego."""
    print("=========================================")
    print("      JUEGO PIEDRA, PAPEL O TIJERA      ")
    print("=========================================")
    print("Opciones disponibles: piedra, papel, tijera")
    print("Modalidad: mejor de 3 rondas")
    print("Gana quien llegue primero a 2 puntos")
    print("=========================================\n")


def pedir_jugada():
    """Solicita y valida la jugada del usuario."""
    jugador = input("Elige una opción: ").lower().strip()

    while jugador not in opciones:
        print("Error: opción no válida. Intenta otra vez.")
        jugador = input("Elige piedra, papel o tijera: ").lower().strip()

    return jugador


def generar_jugada_computadora():
    """Genera una jugada aleatoria para la computadora."""
    return random.choice(opciones)


def determinar_ganador(jugador, computadora):
    """Determina el ganador de una ronda."""
    if jugador == computadora:
        return "empate"

    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "jugador"

    else:
        return "computadora"


def mostrar_resultado_ronda(jugador, computadora, resultado):
    """Muestra las jugadas y el resultado de la ronda."""
    print("\n---------- RESULTADO DE LA RONDA ----------")
    print(f"Jugador eligió: {jugador}")
    print(f"Computadora eligió: {computadora}")

    if resultado == "empate":
        print("Resultado: EMPATE")

    elif resultado == "jugador":
        print("Resultado: GANA EL JUGADOR")

    else:
        print("Resultado: GANA LA COMPUTADORA")


def jugar_partida():
    """Controla una partida completa al mejor de 3."""
    puntos_jugador = 0
    puntos_computadora = 0
    ronda = 1

    while puntos_jugador < 2 and puntos_computadora < 2:
        print(f"\n================ RONDA {ronda} ================")

        jugador = pedir_jugada()
        computadora = generar_jugada_computadora()
        resultado = determinar_ganador(jugador, computadora)

        mostrar_resultado_ronda(jugador, computadora, resultado)

        # Actualización del marcador
        if resultado == "jugador":
            puntos_jugador += 1
            ronda += 1

        elif resultado == "computadora":
            puntos_computadora += 1
            ronda += 1

        else:
            print("El empate no suma puntos. Se repite la ronda.")

        print("\n-------------- MARCADOR ACTUAL --------------")
        print(f"Jugador: {puntos_jugador}")
        print(f"Computadora: {puntos_computadora}")

    print("\n=========================================")
    print("             RESULTADO FINAL             ")
    print("=========================================")

    if puntos_jugador > puntos_computadora:
        print("¡FELICIDADES! Ganaste la partida.")
    else:
        print("La computadora ganó la partida.")

    print(f"Marcador final: Jugador {puntos_jugador} - Computadora {puntos_computadora}")


def preguntar_reinicio():
    """Pregunta al usuario si desea jugar otra partida."""
    respuesta = input("\n¿Deseas jugar otra vez? Escribe si/no: ").lower().strip()

    while respuesta != "si" and respuesta != "no":
        print("Opción no válida.")
        respuesta = input("¿Deseas jugar otra vez? Escribe si/no: ").lower().strip()

    return respuesta


def main():
    """Función principal del programa."""
    jugar_otra_vez = "si"

    while jugar_otra_vez == "si":
        mostrar_bienvenida()
        jugar_partida()
        jugar_otra_vez = preguntar_reinicio()

    print("\nGracias por jugar.")
    print("Programa finalizado.")


# Inicio del programa
if __name__ == "__main__":
    main()
