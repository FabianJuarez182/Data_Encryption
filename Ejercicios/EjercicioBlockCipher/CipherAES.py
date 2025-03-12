from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import numpy as np
from PIL import Image

# Función para generar clave aleatoria de 256 bits (32 bytes)
def generate_key():
    return get_random_bytes(32)

# Función para generar un IV aleatorio de 128 bits (16 bytes)
def generate_iv():
    return get_random_bytes(16)

# Asegurar que el array pueda ser dividido en bloques de 16 bytes
def pad_image_array(image_array):
    flat_pixels = image_array.flatten()
    padded_pixels = pad(flat_pixels.tobytes(), AES.block_size)
    return np.frombuffer(padded_pixels, dtype=np.uint8)

# Función para cifrar una imagen con AES en modo CBC
def encrypt_aes_cbc(image_array, key):
    iv = generate_iv()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_pixels = pad_image_array(image_array)
    ciphertext = cipher.encrypt(padded_pixels.tobytes())
    encrypted_pixels = np.frombuffer(ciphertext, dtype=np.uint8)
    return reshape_to_image(encrypted_pixels, image_array.shape)

# Función para cifrar una imagen con AES en modo ECB
def encrypt_aes_ecb(image_array, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_pixels = pad_image_array(image_array)
    ciphertext = cipher.encrypt(padded_pixels.tobytes())
    encrypted_pixels = np.frombuffer(ciphertext, dtype=np.uint8)
    return reshape_to_image(encrypted_pixels, image_array.shape)

# Ajustar los datos cifrados al tamaño de la imagen original
def reshape_to_image(data, shape):
    total_pixels = np.prod(shape)
    trimmed_data = data[:total_pixels]
    reshaped = np.reshape(trimmed_data, shape)
    return reshaped.astype(np.uint8)

# Leer imagen y convertirla a array RGB
def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    return np.array(img)

# Guardar imagen desde array RGB
def save_image(image_array, path):
    img = Image.fromarray(image_array, 'RGB')
    img.save(path)

# Ejecución principal
if __name__ == "__main__":
    image_path = "./pic.png"
    image_array = load_image(image_path)
    key = generate_key()

    # CBC
    encrypted_cbc = encrypt_aes_cbc(image_array, key)
    save_image(encrypted_cbc, "encrypted_cbc_image.png")
    print("Imagen encriptada CBC guardada como 'encrypted_cbc_image.png'")

    # ECB
    encrypted_ecb = encrypt_aes_ecb(image_array, key)
    save_image(encrypted_ecb, "encrypted_ecb_image.png")
    print("Imagen encriptada ECB guardada como 'encrypted_ecb_image.png'")

    print("Proceso finalizado. Revisa las imágenes resultantes.")
