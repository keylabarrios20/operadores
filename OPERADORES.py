import math

def resolver_ecuacion_cuadratica(a, b, c):
    # Calcula el discriminante
    discriminante = b**2 - 4*a*c

    # Verifica si el discriminante es negativo
    if discriminante < 0:
        return None  # No hay soluciones reales

    # Calcula las soluciones utilizando la fórmula cuadrática
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)

    return x1, x2

# Pide al usuario que ingrese los coeficientes
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
c = float(input("Ingrese el coeficiente 'c': "))

# Resuelve la ecuación cuadrática
soluciones = resolver_ecuacion_cuadratica(a, b, c)

# Muestra los resultados
if soluciones is None:
    print("La ecuación cuadrática no tiene soluciones reales.")
else:
    x1, x2 = soluciones
    print(f"Solución 1: {x1}")
    print(f"Solución 2: {x2}")
