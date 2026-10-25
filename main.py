# Juego de adivinanza
import random

print("=== JUEGO DE ADIVINANZA ===")

# El programa elige un número al azar entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos_max = 7
intentos = 0
adivinado = False

print(f"Adivina el número del 1 al 100, tienes {intentos_max} intentos.")

# Se repite hasta que acierte o se acaben los intentos
while intentos < intentos_max and not adivinado:
    intento = int(input("Tu número: "))
    intentos = intentos + 1

    # Comparamos con el número secreto y damos pista
    if intento == numero_secreto:
        adivinado = True
    elif intento < numero_secreto:
        print("Pista: el número es mayor.")
    else:
        print("Pista: el número es menor.")

# Mostramos el resultado final
if adivinado:
    print(f"¡Ganaste! Era el {numero_secreto} y lo adivinaste en {intentos} intentos.")
else:
    print(f"Perdiste, el número era {numero_secreto}.")