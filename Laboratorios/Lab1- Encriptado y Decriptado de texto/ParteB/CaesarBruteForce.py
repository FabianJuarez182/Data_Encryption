'''
 * Nombre: CaesarBruteForce.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 03.02.2025
'''
import Util

def encriptar(texto, desplazamiento=3):
    resultado = ""
    longitud_diccionario = len(Util.Diccionario)
    # Recorrer cada letra del texto
    for letra in texto.lower():
        # Si es una letra, la desplazamos
        if letra in Util.Diccionario:
            indice_actual = Util.Diccionario.index(letra)
            # Obtener el nuevo caracter
            nueva_posicion = (indice_actual + desplazamiento) % longitud_diccionario
            # Se arma el nuevo texto
            resultado += Util.Diccionario[nueva_posicion]
        else:
            # Si no es letra, la dejamos igual
            resultado += letra
    return resultado

def desencriptar(texto, desplazamiento=3):
    # Para desencriptar, usamos el desplazamiento negativo
    return encriptar(texto, -desplazamiento)

def ataque_fuerza_bruta(mensaje, repeticiones):
    """
    Prueba todas las claves posibles y devuelve las k mejores según el análisis de frecuencia.
    Retorna una lista de tuplas (clave, mensaje_descifrado, metrica)
    """
    resultados = []
    
    # Probar todas las claves posibles (0 a 30)
    for clave in range(repeticiones):
        # Desencriptar el mensaje con la clave actual
        mensaje_descifrado = desencriptar(mensaje, clave)
        
        # Calcular las frecuencias del mensaje descifrado
        frecuencias = Util.analizar_frecuencia(mensaje_descifrado)
        
        # Calcular la métrica (qué tan cerca está de la distribución teórica)
        metrica = Util.calcular_metrica(frecuencias)
        
        # Guardar el resultado
        resultados.append((clave, mensaje_descifrado, metrica))
    
    # Ordenar los resultados por la métrica (menor es mejor)
    resultados_ordenados = sorted(resultados, key=lambda x: x[2])
    
    # Devolver las k mejores claves
    return resultados_ordenados


mensaje = Util.leer_archivo("ceasar.txt")
# Obtener las 30 repeticiones
mejores_resultados = ataque_fuerza_bruta(mensaje, 31)

print(f"\nMensaje original cifrado: {mensaje}")
print("\n=== Mejores Resultados ===")
for clave, letra, texto_descifrado in sorted(mejores_resultados, key=lambda x: x[2], reverse=True):
    print(f"\nClave: {clave}, Letra más frecuente en el texto cifrado: {letra} ")
    print(f"Texto descifrado: {texto_descifrado}")