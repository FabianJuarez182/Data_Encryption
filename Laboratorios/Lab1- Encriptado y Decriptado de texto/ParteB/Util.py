import os
Diccionario = 'abcdefghijklmnñopqrstuvwxyz'

def obtener_distribucion_teorica():
    """Retorna la distribución teórica de frecuencias del español"""
    return {
        'a': 0.1253, 'b': 0.0142, 'c': 0.0468, 'd': 0.0586, 'e': 0.1368,
        'f': 0.0069, 'g': 0.0101, 'h': 0.0070, 'i': 0.0625, 'j': 0.0044,
        'k': 0.0002, 'l': 0.0497, 'm': 0.0315, 'n': 0.0671, 'ñ': 0.0031,
        'o': 0.0868, 'p': 0.0251, 'q': 0.0088, 'r': 0.0687, 's': 0.0798,
        't': 0.0463, 'u': 0.0393, 'v': 0.0090, 'w': 0.0001, 'x': 0.0022,
        'y': 0.0090, 'z': 0.0052
    }

def analizar_frecuencia(texto):
    """Analiza la frecuencia de cada carácter en el texto"""
    # Convertir texto a minúsculas y filtrar solo caracteres del diccionario
    texto = texto.lower()
    texto_filtrado = ''.join(c for c in texto if c in Diccionario)
    
    # Contar total de caracteres válidos
    total_caracteres = len(texto_filtrado)
    
    # Crear diccionario con todas las letras inicializadas en 0
    frecuencias = {letra: 0 for letra in Diccionario}
    
        # Contar frecuencias manualmente
    for letra in texto_filtrado:
        frecuencias[letra] += 1
    
    # Actualizar frecuencias y calcular probabilidades
    for letra in frecuencias:
        frecuencias[letra] = frecuencias[letra] / total_caracteres if total_caracteres > 0 else 0
    
    return frecuencias

def calcular_metrica(frecuencias_texto):
    """Calcula la diferencia entre la distribución del texto y la teórica"""
    dist_teorica = obtener_distribucion_teorica()
    diferencia_total = 0
    
    for letra in Diccionario:
        diferencia = abs(frecuencias_texto[letra] - dist_teorica[letra])
        diferencia_total += diferencia
    
    return diferencia_total

def leer_archivo(nombre_archivo):
        # Obtener la ruta absoluta del script
    ruta_script = os.path.abspath(__file__)

    # Obtener el directorio raíz del script
    raiz = os.path.dirname(ruta_script)

    # Construir la ruta completa del archivo
    ruta_archivo = os.path.join(raiz, "Cifrados", nombre_archivo)

    # Intentar abrir el archivo
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            mensaje = file.read()
            print("Archivo leído correctamente.")
            return mensaje
    except FileNotFoundError:
        print("Error: No se encontró el archivo en la ruta:", ruta_archivo)