
def xor_operation(data, key):
    # Convertir la clave a bytes si es una cadena
    if isinstance(key, str):
        key = key.encode()
    
    print(f"Longitud de los datos: {len(data)}")
    print(f"Longitud de la clave original: {len(key)}")
    
    # Extender la clave para que coincida con la longitud de los datos
    key_repeated = key * (len(data) // len(key)) + key[:len(data) % len(key)]
    print(f"Longitud de la clave extendida: {len(key_repeated)}")
    
    # Realizar operación XOR
    return bytes(a ^ b for a, b in zip(data, key_repeated))

def decode_xor_image(imagen_path, clave):
    try:
        # Leer la imagen corrupta
        with open(imagen_path, 'rb') as img_file:
            imagen_bytes = img_file.read()
        
        print(f"Leyendo imagen corrupta de tamaño: {len(imagen_bytes)} bytes")
        
        # Aplicar XOR directamente con la clave extendida
        resultado_xor = xor_operation(imagen_bytes, clave)
        
        # Guardar el resultado
        with open('imagen_original.png', 'wb') as f:
            f.write(resultado_xor)
        
        print("Archivo guardado exitosamente")
        
    except Exception as e:
        print(f"Error en el proceso: {str(e)}")
        raise

# Uso del script
clave = "cifrados_2025"
ruta_imagen = "imagen_xor.png"  # Asegúrate de que este sea el nombre correcto de tu archivo

try:
    decode_xor_image(ruta_imagen, clave)
    print("¡Imagen descifrada exitosamente! Guardada como 'imagen_original.png'")
except Exception as e:
    print(f"Ocurrió un error: {str(e)}")