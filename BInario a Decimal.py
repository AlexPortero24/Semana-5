# Inicio del Programa de Binario a Decimal

try:  # Intentamos ejecutar el bloque que puede fallar si el usuario ingresa algo incorrecto

    binario = input("Ingrese un número binario (puede tener punto para fracción): ")
    # Guardamos la entrada como string porque el usuario puede ingresar "101.101" y necesitamos manipular los caracteres

    if "." in binario:
        bin_entera, bin_decimal = binario.split(".")
        # split(".") divide la cadena en dos partes usando el punto
        # Por qué: necesitamos procesar la parte entera y la fraccionaria por separado, ya que sus potencias de 2 son distintas
    else:
        bin_entera = binario  # Si no hay punto, toda la cadena es la parte entera
        bin_decimal = ""      # No hay parte decimal, entonces dejamos vacío para no generar error

    decimal_entera = 0
    potencia = len(bin_entera) - 1  # len() nos da cuántos bits tiene la parte entera
    # Por qué: el bit más a la izquierda tiene el valor 2^(n-1) y vamos disminuyendo la potencia a medida que avanzamos
    for digito in bin_entera:
        decimal_entera += int(digito) * (2 ** potencia)
        # Por qué: cada dígito '0' o '1' multiplica su peso según la posición (bitweight)
        potencia -= 1  # Por qué: la siguiente posición vale la mitad, o sea 2^(potencia-1)

    decimal_fraccion = 0.0
    potencia = -1  # El primer bit después del punto vale 2^-1
    for digito in bin_decimal:
        decimal_fraccion += int(digito) * (2 ** potencia)
        # Por qué: en la parte decimal, los bits tienen valores fraccionarios: 2^-1, 2^-2, etc.
        potencia -= 1  # Por qué: cada bit siguiente vale la mitad del anterior

    resultado = decimal_entera + decimal_fraccion
    # Por qué: sumamos parte entera y fraccionaria para obtener el valor decimal completo

    print("El número en decimal es:", resultado)
    # Por qué: mostramos el resultado final al usuario

except ValueError:  # Captura errores si se ingresan caracteres que no son 0 o 1
    print("Error: Debe ingresar un número binario válido (solo 0 y 1).")
    # Por qué: evita que el programa se rompa y da un mensaje claro al usuario
