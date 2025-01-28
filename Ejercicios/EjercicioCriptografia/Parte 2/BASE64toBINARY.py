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

def main():
    # Entrada del usuario
    texto = "Hola"
    
    # Convertir texto a Base64
    texto_base64 = texto_a_base64(texto)
    
    # Convertir Base64 a binario
    binario_base64 = base64_a_binario(texto_base64)
    
    # Mostrar resultados
    print(f"Texto: {texto}")
    print(f"Base64: {texto_base64}")
    print(f"Binario: {binario_base64}")

if __name__ == "__main__":
    main()
