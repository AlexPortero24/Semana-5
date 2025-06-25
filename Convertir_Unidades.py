# El Programa es un conversor de temperaturas.

# El programa tiene como finalidad pasar de grados Celsius a Fahrenheit y Kelvin.

# La idea surgió con el propósito de facilitar la conversión de unidades en la materia de Física 2.
# otra asignatura que también estamos cursando.

# Función que convierte de Celsius a Fahrenheit
# Aquí se utiliza snake_case para el nombre de la función: celsius_a_fahrenheit
def celsius_a_fahrenheit(grados_celsius):  # grados_celsius es tipo float
    return (grados_celsius * 9/5)+32   # El resultado también es un float

# Función que convierte de Celsius a Kelvin
# También usa snake_case para el nombre de la función: celsius_a_kelvin
def celsius_a_kelvin(grados_celsius):  # grados_celsius es float
    return grados_celsius+273.15     # Retorna un float
