'''
 * Nombre: Cipher3DES.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSC
 * Historial: 
    - Finalizado el 11.03.2025
'''
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Función para generar una clave válida para 3DES (24 bytes)
def generar_clave():
    while True:
        clave = get_random_bytes(24)  # 3DES usa una clave de 24 bytes
        try:
            DES3.adjust_key_parity(clave)
            return clave
        except ValueError:
            continue

# Función para cifrar un mensaje con 3DES modo CBC
def cifrar_3des(mensaje):
    clave = generar_clave()
    iv = get_random_bytes(8)  # Vector de inicialización de 8 bytes para CBC
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    mensaje_cifrado = cipher.encrypt(pad(mensaje.encode('utf-8'), DES3.block_size))
    return clave, iv, mensaje_cifrado

# Función para descifrar un mensaje cifrado con 3DES modo CBC
def descifrar_3des(clave, iv, mensaje_cifrado):
    cipher = DES3.new(clave, DES3.MODE_CBC, iv)
    mensaje_descifrado = unpad(cipher.decrypt(mensaje_cifrado), DES3.block_size)
    return mensaje_descifrado.decode('utf-8')

# Prueba de las funciones
mensaje = """The main weakness of DES is its short key. It thus makes sense to try to
design a block cipher with a larger key length using DES as a building block.
Some approaches to doing so are discussed in this section. Although we refer
to DES frequently throughout the discussion, and DES is the most prominent
block cipher to which these techniques have been applied, everything we say
here applies generically to any block cipher."""
clave, iv, mensaje_cifrado = cifrar_3des(mensaje)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_3des(clave, iv, mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)



