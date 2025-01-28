def decimal_a_binario(decimal):
    # Lista para almacenar los dígitos binarios
    digitos_binarios = []
    
    # Si el número es 0, retornar directamente '00000000'
    if decimal == 0:
        return '00000000'
    
    # Proceso de división sucesiva entre 2
    while decimal > 0:
        residuo = decimal % 2
        digitos_binarios.insert(0, str(residuo))
        decimal = decimal // 2
    
    # Asegurar que el resultado tenga 8 bits
    while len(digitos_binarios) < 8:
        digitos_binarios.insert(0, '0')
    
    return ''.join(digitos_binarios)

def ascii_a_binario(texto):
    # Lista para almacenar los valores ASCII y binarios
    ascii_binarios = []
    binario_completo = []  # Lista para el binario completo final
    
    # Convertir cada carácter a su representación ASCII y binaria
    for caracter in texto:
        # Obtener el valor ASCII del carácter
        valor_ascii = ord(caracter)
        # Convertir el valor ASCII a binario
        valor_binario = decimal_a_binario(valor_ascii)
        # Guardar el carácter, su ASCII y su binario
        ascii_binarios.append((caracter, valor_ascii, valor_binario))
        # Agregar el binario al binario completo
        binario_completo.append(valor_binario)
    
    # Unir todos los valores binarios para el binario completo
    binario_completo = ' '.join(binario_completo)
    
    return ascii_binarios, binario_completo

# Función principal
def main():
    # Entrada del usuario
    texto = "Hola"
    
    # Convertir texto
    ascii_binarios, binario_completo = ascii_a_binario(texto)
    
    # Mostrar resultados
    print(f"\nTexto original: {texto}")
    print("\nCarácter | ASCII | Binario")
    print("--------------------------")
    for caracter, valor_ascii, valor_binario in ascii_binarios:
        print(f"   {caracter}     |  {valor_ascii:3}  | {valor_binario}")
    
    # Mostrar el binario completo
    print("\nBinario completo del texto:")
    print(binario_completo)
    print()

# Ejecutar el programa
if __name__ == "__main__":
    main()