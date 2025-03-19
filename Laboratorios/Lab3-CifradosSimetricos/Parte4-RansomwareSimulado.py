from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Clave de cifrado (debe ser de 16, 24 o 32 bytes)
KEY = b'mi_clave_secreta'
IV = b'1234567890123456'  # IV de 16 bytes

def encrypt_file(file_path):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(file_path + '.enc', 'wb') as f:
        f.write(ciphertext)
    os.remove(file_path)  # Borrar el archivo original

def encrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if not filename.endswith('.enc'):
                encrypt_file(file_path)

def decrypt_file(file_path):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    with open(file_path, 'rb') as f:
        ciphertext = f.read()
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    original_path = file_path.replace('.enc', '')
    with open(original_path, 'wb') as f:
        f.write(plaintext)
    os.remove(file_path)  # Borrar el archivo cifrado

def decrypt_directory(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.endswith('.enc'):
                decrypt_file(file_path)

if __name__ == "__main__":
    folder = input("Ingresa la carpeta a cifrar/descifrar: ")
    action = input("¿Cifrar (E) o Descifrar (D)? ").strip().upper()
    if action == 'E':
        encrypt_directory(folder)
        print("Archivos cifrados exitosamente.")
    elif action == 'D':
        decrypt_directory(folder)
        print("Archivos descifrados exitosamente.")
    else:
        print("Opción no válida.")
