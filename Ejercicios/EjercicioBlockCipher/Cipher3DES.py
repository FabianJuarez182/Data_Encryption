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
mensaje = """The DES block cipher is a 16-round Feistel network with a block length of
64 bits and a key length of 56 bits. The same round function ˆ f is used in each
of the 16 rounds. The round function takes a 48-bit sub-key and, as expected
for a (balanced) Feistel network, a 32-bit input (namely, half a block). The
key schedule of DES is used to derive a sequence of 48-bit sub-keys k1, . . . , k16
from the 56-bit master key."""
clave, iv, mensaje_cifrado = cifrar_3des(mensaje)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_3des(clave, iv, mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)



