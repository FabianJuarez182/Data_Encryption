'''
 * Nombre: GeneracionKeystream.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: Cursor
 * Historial: 
    - Finalizado el 24.02.2025
'''

def custom_hash(input_string):
    """
    Función hash simple para generar un valor numérico a partir de una cadena.
    Esto es una implementación muy básica y no debe usarse para seguridad real.
    """
    hash_value = 0
    for char in input_string:
        # Rotación simple y mezcla
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF  # Mantener en 32 bits
    return hash_value

class CustomPRNG:
    """
    Generador de números pseudoaleatorios personalizado
    Implementa un generador congruencial lineal (LCG) simple
    """
    def __init__(self, seed):
        # Parámetros del LCG
        self.modulus = 2**31 - 1  # Un número primo grande (Mersenne)
        self.multiplier = 48271   # Valor random
        self.increment = 0        # Para un generador multiplicativo puro
        
        # Inicializar estado con la semilla
        self.state = seed % self.modulus
        if self.state == 0:
            self.state = 1  # Evitar el estado 0 para complicaciones futuras
        
        # Realizar algunos ciclos iniciales para mejorar la distribución
        for _ in range(10):
            self.next_int()
    
    def next_int(self):
        """Genera el siguiente número entero pseudoaleatorio"""
        self.state = (self.multiplier * self.state + self.increment) % self.modulus
        return self.state
    
    def next_byte(self):
        """Genera un byte pseudoaleatorio (0-255)"""
        return self.next_int() % 256

def generate_keystream(seed_str, message_length):
    """
    Genera un keystream pseudoaleatorio basado en un valor semilla.
    
    Args:
        seed_str (str): Semilla o clave para inicializar el PRNG
        message_length (int): Longitud del mensaje a cifrar
    
    Returns:
        list: Keystream de bytes pseudoaleatorios
    """
    # Convertir la cadena de semilla en un valor numérico usando nuestra función hash
    seed_value = custom_hash(seed_str)
    
    # Inicializar nuestro PRNG personalizado
    prng = CustomPRNG(seed_value)
    
    # Generar el keystream
    keystream = []
    for _ in range(message_length):
        keystream.append(prng.next_byte())
    
    return keystream

# Función auxiliar para convertir el keystream a formato hexadecimal
def bytes_to_hex(byte_array):
    return ''.join(f'{byte:02x}' for byte in byte_array)

# Ejemplo de uso
def ejemplo_uso():
    mensaje = "Este es un mensaje secreto"
    clave = "mi_clave_secreta_2024"
    
    # Generamos el keystream
    keystream = generate_keystream(clave, len(mensaje))
    
    print(f"Mensaje original: {mensaje}")
    print(f"Longitud del mensaje: {len(mensaje)}")
    print(f"Keystream generado (hex): {bytes_to_hex(keystream)}")
    print(f"Longitud del keystream: {len(keystream)}")

if __name__ == "__main__":
    ejemplo_uso()