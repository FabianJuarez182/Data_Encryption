'''
 * Nombre: CipherDES.py
 * Programadora: Fabian Juarez (jua21440@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSC
 * Historial: 
    - Finalizado el 06.03.2025
'''
from Crypto.Cipher import DES
import os

def pad(data):
    """Aplica un relleno manual con el caracter '#' hasta alcanzar un múltiplo de 8."""
    pad_len = 8 - (len(data) % 8)
    return data + (b'#' * pad_len)

def unpad(data):
    """Remueve el relleno manual con el caracter '#'"""
    return data.rstrip(b'#')

def generate_key():
    """Genera una clave aleatoria de 8 bytes para DES."""
    return os.urandom(8)

def des_encrypt(plaintext, key):
    """Cifra un mensaje con DES en modo ECB."""
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext)
    return cipher.encrypt(padded_text)

def des_decrypt(ciphertext, key):
    """Descifra un mensaje con DES en modo ECB."""
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data).decode()

def get_full_path(filename):
    """Obtiene la ruta absoluta del archivo."""
    return os.path.join(os.getcwd(), filename)

def read_file(filename):
    """Lee el contenido de un archivo .txt."""
    filepath = get_full_path(filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"El archivo {filepath} no existe.")
    with open(filepath, 'rb') as file:
        return file.read()

# Ejemplo de uso
key = generate_key()
cipher_filename = "des.txt"

# Leer el mensaje desde un archivo
plaintext = read_file(cipher_filename)
ciphertext = des_encrypt(plaintext, key)
decrypted_message = des_decrypt(ciphertext, key)
print ("Texto original: ", plaintext)
print("------------------------------------")
print(f"Clave: {key.hex()}")
print(f"Texto cifrado: {ciphertext.hex()}")
print("------------------------------------")
print(f"Texto descifrado: {decrypted_message}")
