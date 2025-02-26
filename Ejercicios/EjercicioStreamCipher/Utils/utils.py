# Tabla de caracteres Base64
TABLA_BASE64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

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

def imprimir_texto_ascii_bin(texto,ascii_binarios, binario_completo ):
     # Mostrar resultados
    print(f"\nTexto original: {texto}")
    print("\nCarácter | Binario")
    print("--------------------------")
    for caracter, valor_ascii, valor_binario in ascii_binarios:
        print(f"   {caracter} | {valor_binario}")
    
    # Mostrar el binario completo
    print("\nBinario completo del texto:")
    print(binario_completo)
    print()

# Bytes a cadenas

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

# bin a Base 64

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

# Base 64 a ASCII

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
    
def printBase64_to_ascii(texto_base64):
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

# XOR

class CifradoXOR:
    def texto_a_binario(self, texto):
        """Convierte texto a su representación binaria"""
        return ''.join(format(ord(char), '08b') for char in texto)
    
    def binario_a_texto(self, binario):
        """Convierte una cadena binaria a texto"""
        bytes_lista = [binario[i:i+8] for i in range(0, len(binario), 8)]
        return ''.join(chr(int(byte, 2)) for byte in bytes_lista)
    
    def xor_binario(self, bin1, bin2):
        """Realiza XOR bit a bit entre dos cadenas binarias"""
        resultado = ''
        for b1, b2 in zip(bin1, bin2):
            resultado += '1' if b1 != b2 else '0'
        return resultado
    
    def cifrar(self, mensaje, llave):
        """Cifra el mensaje usando XOR con la llave ajustada"""        
        # Convertir mensaje y llave a binario
        mensaje_bin = self.texto_a_binario(mensaje)
        llave_bin = self.texto_a_binario(llave)
        
        # Realizar XOR
        resultado_bin = self.xor_binario(mensaje_bin, llave_bin)
        
        return self.binario_a_texto(resultado_bin)
    
    def descifrar(self, texto_cifrado, llave):
        """
        Descifra el mensaje que fue cifrado con XOR.
        Dado que XOR es simétrico, el proceso es idéntico al cifrado.
        """
        return self.cifrar(texto_cifrado, llave)
# Función auxiliar para convertir el keystream a formato hexadecimal
def bytes_to_hex(byte_array):
    return ''.join(f'{byte:02x}' for byte in byte_array)