'''
 * Nombre: AfínBruteForce.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 03.02.2025
'''
import Util

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
    m = len(Util.Diccionario)
    
    if not validar_clave(a, m):
        raise ValueError(f"'a' ({a}) debe ser coprimo con {m}")
    
    for letra in texto.lower():
        if letra in Util.Diccionario:
            # Obtener posición de la letra en el diccionario
            x = Util.Diccionario.index(letra)
            # Aplicar función de cifrado: E(x) = (ax + b) mod m
            nueva_pos = (a * x + b) % m
            resultado += Util.Diccionario[nueva_pos]
        else:
            resultado += letra
    return resultado

def descifrado_afin(texto, a, b):
    """Descifra un texto usando el cifrado afín D(y) = a^(-1)(y - b) mod m"""
    resultado = ""
    m = len(Util.Diccionario)
    
    if not validar_clave(a, m):
        raise ValueError(f"'a' ({a}) debe ser coprimo con {m}")
    
    # Calcular el inverso multiplicativo de a
    a_inv = inverso_multiplicativo(a, m)
    if a_inv is None:
        raise ValueError(f"No existe inverso multiplicativo para {a}")
    
    for letra in texto.lower():
        if letra in Util.Diccionario:
            # Obtener posición de la letra en el diccionario
            y = Util.Diccionario.index(letra)
            # Aplicar función de descifrado: D(y) = a^(-1)(y - b) mod m
            x = (a_inv * (y - b)) % m
            resultado += Util.Diccionario[x]
        else:
            resultado += letra
    return resultado

def ataque_fuerza_bruta(mensaje, a_max=None, b_max=None):
    """
    Prueba todas las combinaciones de claves posibles y devuelve las mejores según el análisis de frecuencia.
    Retorna una lista de tuplas (a, b, mensaje_descifrado, metrica)
    """
    resultados = []
    m = len(Util.Diccionario)
    
    # Si no se proporcionan a_max y b_max, usar el máximo del diccionario
    a_max = a_max if a_max is not None else m - 1
    b_max = b_max if b_max is not None else m - 1
    
    # Probar todas las combinaciones de a y b
    for a in range(1, a_max + 1):
        # Verificar que a sea coprimo con m
        if not validar_clave(a, m):
            continue
        
        for b in range(b_max + 1):
            try:
                # Desencriptar el mensaje con la clave actual
                mensaje_descifrado = descifrado_afin(mensaje, a, b)
                
                # Calcular las frecuencias del mensaje descifrado
                frecuencias = Util.analizar_frecuencia(mensaje_descifrado)
                
                # Calcular la métrica (qué tan cerca está de la distribución teórica)
                metrica = Util.calcular_metrica(frecuencias)
                
                # Guardar el resultado
                resultados.append((a, b, mensaje_descifrado, metrica))
            except ValueError:
                # Saltar claves inválidas
                continue
    
    # Ordenar los resultados por la métrica (menor es mejor)
    resultados_ordenados = sorted(resultados, key=lambda x: x[3])
    
    # Devolver todos los resultados
    return resultados_ordenados

# Leer el mensaje cifrado
mensaje = Util.leer_archivo("afines.txt")

# Obtener los mejores resultados del ataque de fuerza bruta
# Puedes especificar límites para a y b, o dejarlo por defecto
# mejores_resultados = ataque_fuerza_bruta(mensaje, a_max=10, b_max=10)  # Ejemplo de límites personalizados
mejores_resultados = ataque_fuerza_bruta(mensaje)

print(f"\nMensaje original cifrado: {mensaje}")
print("\n=== Mejores Resultados ===")
for a, b, texto_descifrado, metrica in sorted(mejores_resultados, key=lambda x: x[3], reverse=True):
    print(f"\nClaves: a = {a}, b = {b}")
    print(f"Métrica de similitud: {metrica}")
    print(f"Texto descifrado: {texto_descifrado}")
