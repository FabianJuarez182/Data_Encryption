import time
import os
from Crypto.Cipher import ChaCha20, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import tracemalloc

# Generar clave y nonce para ChaCha20 y AES
key_chacha = get_random_bytes(32)  # ChaCha20 usa clave de 256 bits
nonce_chacha = get_random_bytes(12)  # Nonce de 12 bytes para ChaCha20

key_aes = get_random_bytes(32)  # AES-256
iv_aes = get_random_bytes(16)  # IV de 16 bytes para AES CBC

message = b"Este es un mensaje secreto que se cifrara y descifrara" * 100  # Mensaje de prueba

# Funciones para cifrado y descifrado con ChaCha20
def encrypt_chacha20(msg):
    cipher = ChaCha20.new(key=key_chacha, nonce=nonce_chacha)
    return cipher.encrypt(msg)

def decrypt_chacha20(ciphertext):
    cipher = ChaCha20.new(key=key_chacha, nonce=nonce_chacha)
    return cipher.decrypt(ciphertext)

# Funciones para cifrado y descifrado con AES-CBC
def encrypt_aes(msg):
    cipher = AES.new(key_aes, AES.MODE_CBC, iv_aes)
    return cipher.encrypt(pad(msg, AES.block_size))

def decrypt_aes(ciphertext):
    cipher = AES.new(key_aes, AES.MODE_CBC, iv_aes)
    return unpad(cipher.decrypt(ciphertext), AES.block_size)

# Medición de rendimiento
tracemalloc.start()
start_time = time.time()
encrypted_chacha = encrypt_chacha20(message)
decrypted_chacha = decrypt_chacha20(encrypted_chacha)
chacha_time = time.time() - start_time
chacha_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
start_time = time.time()
encrypted_aes = encrypt_aes(message)
decrypted_aes = decrypt_aes(encrypted_aes)
aes_time = time.time() - start_time
aes_mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

# Resultados
print(f"Tiempo de ChaCha20: {chacha_time:.6f} segundos, Memoria usada: {chacha_mem} bytes")
print(f"Tiempo de AES-CBC: {aes_time:.6f} segundos, Memoria usada: {aes_mem} bytes")

# Validación de los mensajes descifrados
assert message == decrypted_chacha, "Error en descifrado con ChaCha20"
assert message == decrypted_aes, "Error en descifrado con AES"

print("Cifrado y descifrado exitosos para ambos algoritmos")