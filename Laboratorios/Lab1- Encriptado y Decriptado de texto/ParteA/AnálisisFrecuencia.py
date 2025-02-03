'''
 * Nombre: AnálisisFrecuencia.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 03.02.2025
'''

import matplotlib.pyplot as plt

Diccionario = 'abcdefghijklmnñopqrstuvwxyz'

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

def mostrar_resultados(frecuencias):
    """Muestra los resultados del análisis de frecuencia"""
    print("\nAnálisis de Frecuencia:")
    print("------------------------")
    for letra, prob in frecuencias.items():
        print(f"Letra '{letra}': {prob:.4f} ({prob*100:.2f}%)")

def graficar_frecuencias(frecuencias):
    """Genera un gráfico de barras con las frecuencias"""
    plt.figure(figsize=(15, 5))
    plt.bar(frecuencias.keys(), frecuencias.values())
    plt.title('Distribución de Frecuencias de Caracteres')
    plt.xlabel('Caracteres')
    plt.ylabel('Frecuencia Relativa')
    plt.show()

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

def comparar_distribuciones(frecuencias_texto):
    """Compara la distribución del texto con la distribución teórica"""
    dist_teorica = obtener_distribucion_teorica()
    
    print("\nComparación con distribución teórica:")
    print("-------------------------------------")
    print("Letra | Texto  | Teórica | Diferencia")
    print("------------------------------------")
    
    for letra in Diccionario:
        freq_texto = frecuencias_texto[letra] * 100
        freq_teorica = dist_teorica[letra] * 100
        diferencia = (freq_texto - freq_teorica)
        print(f"{letra:5} | {freq_texto:6.4f}% | {freq_teorica:6.4f}% | {diferencia:8.4f}%")
def graficar_comparacion_distribuciones(frecuencias_texto):
    """Genera un gráfico comparativo entre la distribución del texto y la teórica"""
    dist_teorica = obtener_distribucion_teorica()
    
    # Preparar datos para la gráfica
    letras = list(Diccionario)
    freq_texto = [frecuencias_texto[letra] for letra in letras]
    freq_teorica = [dist_teorica[letra] for letra in letras]
    
    # Configurar el tamaño de la figura
    plt.figure(figsize=(15, 6))
    
    # Crear gráfico de barras agrupadas
    x = range(len(letras))
    ancho = 0.35
    
    plt.bar([i - ancho/2 for i in x], freq_texto, ancho, label='Texto Analizado', color='skyblue')
    plt.bar([i + ancho/2 for i in x], freq_teorica, ancho, label='Distribución Teórica', color='lightcoral')
    
    # Personalizar el gráfico
    plt.xlabel('Letras')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Comparación de Distribuciones de Frecuencia')
    plt.xticks(x, letras)
    plt.legend()
    
    # Ajustar el diseño para evitar que se corten las etiquetas
    plt.tight_layout()
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    texto_ejemplo = """Este es un texto de ejemplo para analizar la frecuencia
                      de aparición de cada letra en español. Incluye números 123
                      y símbolos !@# que serán ignorados en el análisis."""
    
    frecuencias = analizar_frecuencia(texto_ejemplo)
    mostrar_resultados(frecuencias)
    comparar_distribuciones(frecuencias)
    graficar_comparacion_distribuciones(frecuencias) 