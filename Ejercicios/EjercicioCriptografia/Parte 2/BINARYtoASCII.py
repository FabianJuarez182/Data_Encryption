def texto_a_binario(texto):
    # Función auxiliar para convertir un número decimal a binario manualmente
    def decimal_a_binario(decimal, bits=8):
        binario = ""
        while decimal > 0:
            binario = str(decimal % 2) + binario  # Obtener el bit menos significativo
            decimal //= 2  # Reducir el número dividiendo por 2
        
        # Asegurar que el resultado tenga la longitud deseada (rellenar con ceros a la izquierda)
        while len(binario) < bits:
            binario = "0" + binario
        
        return binario
    
    # Convertir cada carácter del texto en su código ASCII y luego a binario
    resultado_binario = []
    for caracter in texto:
        codigo_ascii = ord(caracter)  # Obtener el código ASCII del carácter
        binario = decimal_a_binario(codigo_ascii)  # Convertir a binario manualmente
        resultado_binario.append(binario)  # Añadir el binario al resultado
    
    return ' '.join(resultado_binario)  # Unir los binarios con un espacio

def binario_a_decimal(binario):
    # Convertir string binario a decimal usando potencias de 2
    decimal = 0
    potencia = 0
    
    # Recorremos el binario de derecha a izquierda
    for bit in reversed(binario):
        if bit == '1':
            decimal += 2 ** potencia
        potencia += 1
    
    return decimal

def binario_a_ascii(texto_binario):
    try:
        # Separar los bytes en una lista
        bytes_binarios = texto_binario.split()

        # Convertir cada byte binario a decimal y luego a su carácter ASCII
        caracteres = [chr(binario_a_decimal(byte)) for byte in bytes_binarios]

        # Unir los caracteres en una sola cadena
        return ''.join(caracteres)

    except ValueError as e:
        return f"Error: {str(e)}"


def main():
    texto_binario = "01001000 01101111 01101100 01100001"
    
    # Convertir binario a ASCII
    resultado = binario_a_ascii(texto_binario)
    print(f"Binario: {texto_binario}")
    print(f"\nBinario a ASCII: {resultado}")

if __name__ == "__main__":
    main()