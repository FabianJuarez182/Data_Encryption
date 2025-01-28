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
        # Eliminar espacios si existen
        texto_binario = texto_binario.replace(" ", "")
        
        # Verificar que solo contenga 0s y 1s
        if not all(bit in '01' for bit in texto_binario):
            raise ValueError("El texto debe contener solo 0s y 1s")
        
        # Verificar que la longitud sea múltiplo de 8
        if len(texto_binario) % 8 != 0:
            raise ValueError("La longitud del texto binario debe ser múltiplo de 8")
        
        # Lista para almacenar las posiciones ASCII
        posiciones_ascii = []
        
        # Convertir cada grupo de 8 bits a su correspondiente posición en la tabla ASCII
        for i in range(0, len(texto_binario), 8):
            # Obtener grupo de 8 bits
            byte = texto_binario[i:i+8]
            # Convertir a decimal
            decimal = binario_a_decimal(byte)
            # Almacenar la posición en la tabla ASCII
            posiciones_ascii.append(decimal)
        
        return ' '.join(str(pos) for pos in posiciones_ascii)

    
    except ValueError as e:
        return f"Error: {str(e)}"

def main():
    texto = "Hola"
    
    # Convertir texto a binario
    texto_binario = texto_a_binario(texto)
    print(f"Texto original: {texto}")
    print(f"Binario: {texto_binario}")
    
    # Convertir binario a ASCII
    resultado = binario_a_ascii(texto_binario)
    print(f"\nBinario a ASCII: {resultado}")

if __name__ == "__main__":
    main()