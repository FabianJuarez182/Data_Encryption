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

def texto_a_base64(texto):
    # Convertir texto en binario (8 bits por carácter)
    binario_completo = ''.join([decimal_a_binario(ord(c), bits=8) for c in texto])
    
    # Dividir el binario en bloques de 6 bits (Base64 usa 6 bits por carácter)
    grupos_de_seis = [binario_completo[i:i+6] for i in range(0, len(binario_completo), 6)]
    
    # Asegurar que cada grupo tenga 6 bits (completar con ceros si es necesario)
    if len(grupos_de_seis[-1]) < 6:
        grupos_de_seis[-1] = grupos_de_seis[-1].ljust(6, '0')
    
    # Convertir cada grupo de 6 bits al índice en la tabla Base64
    texto_base64 = ''.join([TABLA_BASE64[int(grupo, 2)] for grupo in grupos_de_seis])
    
    # Agregar padding "=" si es necesario
    while len(texto_base64) % 4 != 0:
        texto_base64 += '='
    
    return texto_base64

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
    print("Conversor de Base64 a ASCII (paso a paso)")
    string = "Hola"
    print("Texto original: ", string)
    texto_base64 = texto_a_base64(string)
    
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