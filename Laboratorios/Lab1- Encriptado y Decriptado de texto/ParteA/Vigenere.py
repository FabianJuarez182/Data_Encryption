'''
 * Nombre: Vigenere.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 30.01.2025
'''
Diccionario = 'abcdefghijklmnñopqrstuvwxyz'

def generar_clave(mensaje, clave):
    """Genera la clave repetida para que coincida con la longitud del mensaje"""
    clave = clave.lower()
    clave_repetida = ""
    j = 0
    
    for i in range(len(mensaje)):
        if mensaje[i] in Diccionario:
            clave_repetida += clave[j % len(clave)]
            j += 1
        else:
            clave_repetida += " "
    return clave_repetida

def cifrado_vigenere(mensaje, clave):
    """Cifra un mensaje usando el cifrado Vigenère"""
    mensaje = mensaje.lower()
    clave_completa = generar_clave(mensaje, clave)
    resultado = ""
    j = 0
    
    for i in range(len(mensaje)):
        if mensaje[i] in Diccionario:
            # Obtener los índices de la letra del mensaje y de la clave
            m = Diccionario.index(mensaje[i])
            k = Diccionario.index(clave_completa[i])
            
            # Aplicar el cifrado: (mi + ki) mod 27
            nueva_pos = (m + k) % len(Diccionario)
            resultado += Diccionario[nueva_pos]
        else:
            resultado += mensaje[i]
            
    return resultado

def descifrado_vigenere(mensaje_cifrado, clave):
    """Descifra un mensaje usando el cifrado Vigenère"""
    mensaje_cifrado = mensaje_cifrado.lower()
    clave_completa = generar_clave(mensaje_cifrado, clave)
    resultado = ""
    
    for i in range(len(mensaje_cifrado)):
        if mensaje_cifrado[i] in Diccionario:
            # Obtener los índices de la letra cifrada y de la clave
            c = Diccionario.index(mensaje_cifrado[i])
            k = Diccionario.index(clave_completa[i])
            
            # Aplicar el descifrado: (ci - ki) mod 27
            nueva_pos = (c - k) % len(Diccionario)
            resultado += Diccionario[nueva_pos]
        else:
            resultado += mensaje_cifrado[i]
            
    return resultado

# Ejemplo de uso
if __name__ == "__main__":
    mensaje = "hola mundo"
    clave = "clave"
    
    mensaje_cifrado = cifrado_vigenere(mensaje, clave)
    mensaje_descifrado = descifrado_vigenere(mensaje_cifrado, clave)
    
    print(f"Mensaje original: {mensaje}")
    print(f"Clave: {clave}")
    print(f"Mensaje cifrado: {mensaje_cifrado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")