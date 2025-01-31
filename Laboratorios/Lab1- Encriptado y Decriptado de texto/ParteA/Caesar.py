'''
 * Nombre: Caesar.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 30.01.2025
'''

Diccionario = 'abcdefghijklmnopqrstuvwxyz'

def encriptar(texto, desplazamiento=3):
    resultado = ""
    longitud_diccionario = len(Diccionario)
    # Recorrer cada letra del texto
    for letra in texto.lower():
        # Si es una letra, la desplazamos
        if letra in Diccionario:
            indice_actual = Diccionario.index(letra)
            # Obtener el nuevo caracter
            nueva_posicion = (indice_actual + desplazamiento) % longitud_diccionario
            # Se arma el nuevo texto
            resultado += Diccionario[nueva_posicion]
        else:
            # Si no es letra, la dejamos igual
            resultado += letra
    return resultado

def desencriptar(texto, desplazamiento=3):
    # Para desencriptar, usamos el desplazamiento negativo
    return encriptar(texto, -desplazamiento)

# Ejemplo de uso
mensaje = "hola mundo"
mensaje_encriptado = encriptar(mensaje)
mensaje_desencriptado = desencriptar(mensaje_encriptado)

print(f"Original: {mensaje}")
print(f"Encriptado: {mensaje_encriptado}")
print(f"Desencriptado: {mensaje_desencriptado}")
