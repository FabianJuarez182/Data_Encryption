'''
 * Nombre: VigenereBruteForce.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 03.02.2025
'''
import Util
import itertools

def generar_clave(mensaje, clave):
    """Genera la clave repetida para que coincida con la longitud del mensaje"""
    clave = clave.lower()
    clave_repetida = ""
    j = 0
    
    for i in range(len(mensaje)):
        if mensaje[i] in Util.Diccionario:
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
        if mensaje[i] in Util.Diccionario:
            # Obtener los índices de la letra del mensaje y de la clave
            m = Util.Diccionario.index(mensaje[i])
            k = Util.Diccionario.index(clave_completa[i])
            
            # Aplicar el cifrado: (mi + ki) mod 27
            nueva_pos = (m + k) % len(Util.Diccionario)
            resultado += Util.Diccionario[nueva_pos]
        else:
            resultado += mensaje[i]
            
    return resultado

def descifrado_vigenere(mensaje_cifrado, clave):
    """Descifra un mensaje usando el cifrado Vigenère"""
    mensaje_cifrado = mensaje_cifrado.lower()
    clave_completa = generar_clave(mensaje_cifrado, clave)
    resultado = ""
    
    for i in range(len(mensaje_cifrado)):
        if mensaje_cifrado[i] in Util.Diccionario:
            # Obtener los índices de la letra cifrada y de la clave
            c = Util.Diccionario.index(mensaje_cifrado[i])
            k = Util.Diccionario.index(clave_completa[i])
            
            # Aplicar el descifrado: (ci - ki) mod 27
            nueva_pos = (c - k) % len(Util.Diccionario)
            resultado += Util.Diccionario[nueva_pos]
        else:
            resultado += mensaje_cifrado[i]
            
    return resultado

def ataque_fuerza_bruta(mensaje, longitud_clave_max=5, palabra_inicial=None):
    """
    Prueba combinaciones de claves para descifrar el mensaje.
    Retorna una lista de resultados ordenados por métrica de similitud.
    
    :param mensaje: Mensaje cifrado
    :param longitud_clave_max: Máxima longitud de la clave a probar
    :param palabra_inicial: Palabra inicial de la clave (opcional)
    :return: Lista de resultados ordenados
    """
    resultados = []
    
    # Usar todas las letras del diccionario
    letras_clave = list(Util.Diccionario)
    
    # Preparar la palabra inicial si se proporciona
    if palabra_inicial:
        # Validar que la palabra inicial use solo letras del diccionario
        palabra_inicial = palabra_inicial.lower()
        if not all(letra in Util.Diccionario for letra in palabra_inicial):
            raise ValueError("La palabra inicial debe contener solo letras del diccionario")
    
    # Probar claves de diferentes longitudes
    for longitud in range(1, longitud_clave_max + 1):
        # Si hay palabra inicial, calcular longitud restante
        if palabra_inicial:
            # Si la palabra inicial es más larga que la longitud máxima, saltar
            if len(palabra_inicial) > longitud:
                continue
            
            # Calcular cuántas letras más necesitamos generar
            letras_restantes = longitud - len(palabra_inicial)
        else:
            # Sin palabra inicial, usar toda la longitud para generar
            letras_restantes = longitud
            palabra_inicial = ""
        
        # Generar todas las combinaciones posibles de letras restantes
        for clave_extra in itertools.product(letras_clave, repeat=letras_restantes):
            # Combinar la palabra inicial con las letras generadas
            clave_completa = palabra_inicial + ''.join(clave_extra)
            
            try:
                # Desencriptar el mensaje con la clave actual
                mensaje_descifrado = descifrado_vigenere(mensaje, clave_completa)
                
                # Calcular las frecuencias del mensaje descifrado
                frecuencias = Util.analizar_frecuencia(mensaje_descifrado)
                
                # Calcular la métrica (qué tan cerca está de la distribución teórica)
                metrica = Util.calcular_metrica(frecuencias)
                
                # Guardar el resultado
                resultados.append((clave_completa, mensaje_descifrado, metrica))
            
            except Exception:
                # Saltar claves problemáticas
                continue
    
    # Ordenar los resultados por la métrica (menor es mejor)
    resultados_ordenados = sorted(resultados, key=lambda x: x[2])
    
    return resultados_ordenados

# Ejemplo de uso
# Leer el mensaje cifrado
mensaje = Util.leer_archivo("vigenere.txt")

# Obtener los mejores resultados del ataque de fuerza bruta
# Con palabra inicial específica
mejores_resultados = ataque_fuerza_bruta(mensaje, longitud_clave_max=6, palabra_inicial='pa')

print(f"\nMensaje original cifrado: {mensaje}")
print("\n=== Mejores Resultados ===")
for clave, texto_descifrado, metrica in mejores_resultados[:10]:  # Mostrar solo los 10 mejores
    print(f"\nClave: {clave}")
    print(f"Métrica de similitud: {metrica}")
    print(f"Texto descifrado: {texto_descifrado}")