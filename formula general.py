# Inicio del Programa de Fórmula General

import math  # Para calcular raíces cuadradas

try:
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))

    if a == 0:
        print("No es una ecuación cuadrática")
    else:
        discriminante = b**2 - 4*a*c  # Calculamos el discriminante

        if discriminante > 0:
            x1 = (-b + math.sqrt(discriminante)) / (2*a)
            x2 = (-b - math.sqrt(discriminante)) / (2*a)
            print(f"Raíces reales y distintas: x1 = {x1}, x2 = {x2}")
        elif discriminante == 0:
            x = -b / (2*a)
            print(f"Raíz real doble: x = {x}")
        else:
            parte_real = -b / (2*a)
            parte_imaginaria = math.sqrt(-discriminante) / (2*a)
            print(f"Raíces complejas: x1 = {parte_real}+{parte_imaginaria}i, x2 = {parte_real}-{parte_imaginaria}i")

except ValueError:
    print("Error: Debe ingresar números válidos")
