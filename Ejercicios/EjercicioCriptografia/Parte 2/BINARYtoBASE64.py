# Tabla de caracteres Base64
TABLA_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

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
    return int(binario, 2)

def agrupar_binario(binario):
    # Eliminar espacios si los hay
    binario = binario.replace(" ", "")
    
    # Asegurar que la longitud sea múltiplo de 6 añadiendo ceros
    while len(binario) % 6 != 0:
        binario += '0'
    
    # Dividir en grupos de 6 bits
    return [binario[i:i+6] for i in range(0, len(binario), 6)]

def binario_a_base64(texto_binario):
    try:
        # Eliminar todos los espacios del binario
        texto_binario = texto_binario.replace(" ", "")
        # Verificar que solo contenga 0s y 1s
        if not all(bit in '01 ' for bit in texto_binario):
            raise ValueError("El texto debe contener solo 0s y 1s")
        
        # Agrupar el binario en grupos de 6 bits
        grupos = agrupar_binario(texto_binario)
        
        # Lista para almacenar los caracteres Base64
        caracteres_base64 = []
        
        # Convertir cada grupo de 6 bits a su correspondiente carácter Base64
        for grupo in grupos:
            # Convertir el grupo binario a decimal
            decimal = binario_a_decimal(grupo)
            # Obtener el carácter Base64 correspondiente
            caracteres_base64.append(TABLA_BASE64[decimal])
        
        # Añadir padding si es necesario
        while len(caracteres_base64) % 4 != 0:
            caracteres_base64.append('=')
        
        return ''.join(caracteres_base64)
    
    except ValueError as e:
        return f"Error: {str(e)}"

def main():
    # Entrada del usuario
    texto = "Hola"
    
    # Convertir texto a binario
    texto_binario = texto_a_binario(texto)
    
    # Convertir binario a Base64
    resultado_base64 = binario_a_base64(texto_binario)
    
    # Mostrar resultados
    print(f"Texto: {texto}")
    print(f"Binario: {texto_binario}")
    print(f"Base64: {resultado_base64}")

if __name__ == "__main__":
    main()
