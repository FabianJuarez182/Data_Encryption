# Tabla de caracteres Base64
TABLA_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def decimal_a_binario(decimal, bits=8):
    # Inicializar la representación binaria como una cadena vacía
    binario = ""
    # Realizar la conversión dividiendo entre 2 y registrando los restos
    while decimal > 0:
        resto = decimal % 2
        binario = str(resto) + binario
        decimal //= 2
    # Asegurar que la representación tenga el número de bits especificado
    binario = binario.zfill(bits)
    return binario

def base64_a_binario(texto_base64):
    # Lista para almacenar los valores binarios
    binario = []
    
    # Procesar cada carácter del texto en Base64 (sin incluir el padding '=')
    for caracter in texto_base64:
        if caracter == '=':
            continue  # Ignorar el relleno
        # Encontrar el índice del carácter en la tabla Base64
        indice = TABLA_BASE64.index(caracter)
        # Convertir el índice a binario (6 bits para cada carácter)
        valor_binario = decimal_a_binario(indice, bits=6)
        binario.append(valor_binario)
    
    # Unir todos los binarios en un solo string
    binario_completo = ''.join(binario)
    
    # Remover los bits sobrantes que no completan un byte
    sobrantes = len(binario_completo) % 8
    if sobrantes != 0:
        binario_completo = binario_completo[:-sobrantes]
    
    # Dividir en grupos de 8 bits para representar bytes
    binario_en_bytes = [binario_completo[i:i+8] for i in range(0, len(binario_completo), 8)]
    
    return ' '.join(binario_en_bytes)

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    
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

        # Unir los caracteres en una sola cadena para formar el texto original
        return ''.join(caracteres)

    except ValueError as e:
        return f"Error: {str(e)}"

def main():
    print("Conversor de Base64 a ASCII (paso a paso)")
    texto_base64 = "SG9sYQ=="
    
    try:
        # Paso 1: Base64 a Binario
        binario = base64_a_binario(texto_base64)
        print(f"\nPaso 1 - Base64 a Binario:")
        print(f"Base64: {texto_base64}")
        print(f"Binario: {binario}")
        
        # Paso 2: Binario a ASCII
        ascii_resultado = binario_a_ascii(binario)
        print(f"\nPaso 2 - Binario a ASCII:")
        print(f"Binario: {binario}")
        print(f"ASCII: {ascii_resultado}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()