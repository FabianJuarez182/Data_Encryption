'''
 * Nombre: Afín.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 30.01.2025
'''

def mcd(a, b):
    """Calcula el máximo común divisor de a y b"""
    while b:
        a, b = b, a % b
    return a

def inverso_multiplicativo(a, m):
    """Calcula el inverso multiplicativo de a módulo m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def validar_clave(a, m):
    """Valida que 'a' sea coprimo con m"""
    return mcd(a, m) == 1

def cifrado_afin(texto, a, b):
    """Encripta un texto usando el cifrado afín E(x) = (ax + b) mod m"""
    resultado = ""
    m = len(Diccionario)
    
    if not validar_clave(a, m):
        raise ValueError(f"'a' ({a}) debe ser coprimo con {m}")
    
    for letra in texto.lower():
        if letra in Diccionario:
            # Obtener posición de la letra en el diccionario
            x = Diccionario.index(letra)
            # Aplicar función de cifrado: E(x) = (ax + b) mod m
            nueva_pos = (a * x + b) % m
            resultado += Diccionario[nueva_pos]
        else:
            resultado += letra
    return resultado

def descifrado_afin(texto, a, b):
    """Descifra un texto usando el cifrado afín D(y) = a^(-1)(y - b) mod m"""
    resultado = ""
    m = len(Diccionario)
    
    if not validar_clave(a, m):
        raise ValueError(f"'a' ({a}) debe ser coprimo con {m}")
    
    # Calcular el inverso multiplicativo de a
    a_inv = inverso_multiplicativo(a, m)
    if a_inv is None:
        raise ValueError(f"No existe inverso multiplicativo para {a}")
    
    for letra in texto.lower():
        if letra in Diccionario:
            # Obtener posición de la letra en el diccionario
            y = Diccionario.index(letra)
            # Aplicar función de descifrado: D(y) = a^(-1)(y - b) mod m
            x = (a_inv * (y - b)) % m
            resultado += Diccionario[x]
        else:
            resultado += letra
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    Diccionario = 'abcdefghijklmnopqrstuvwxyz'
    mensaje = "hola mundo"
    a = 5  # debe ser coprimo con len(Diccionario) = 26
    b = 8
    
    try:
        mensaje_cifrado = cifrado_afin(mensaje, a, b)
        mensaje_descifrado = descifrado_afin(mensaje_cifrado, a, b)
        
        print(f"Mensaje original: {mensaje}")
        print(f"Mensaje cifrado: {mensaje_cifrado}")
        print(f"Mensaje descifrado: {mensaje_descifrado}")
    except ValueError as e:
        print(f"Error: {e}")