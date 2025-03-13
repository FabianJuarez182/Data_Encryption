import os
Diccionario = 'abcdefghijklmnopqrstuvwxyz'

def obtener_distribucion_teorica():
    """Retorna la distribución teórica de frecuencias del español sin letras especiales ni ñ"""
    return {
        'a': 0.11525, 'b': 0.02215, 'c': 0.04019, 'd': 0.05010, 'e': 0.12181,
        'f': 0.00692, 'g': 0.01768, 'h': 0.00703, 'i': 0.06247, 'j': 0.00493,
        'k': 0.00011, 'l': 0.04967, 'm': 0.03157, 'n': 0.06712, 'o': 0.08683,
        'p': 0.02510, 'q': 0.00877, 'r': 0.06871, 's': 0.07977, 't': 0.04632,
        'u': 0.02927, 'v': 0.01138, 'w': 0.00017, 'x': 0.00215, 'y': 0.01008,
        'z': 0.00467
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
        diferencia = ((frecuencias_texto[letra] - dist_teorica[letra]) ** 2) / dist_teorica[letra]
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