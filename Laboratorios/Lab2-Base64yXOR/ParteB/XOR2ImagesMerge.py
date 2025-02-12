from PIL import Image
import numpy as np

def apply_image_xor(image1_path, image2_path, output_path):
    """
    Aplica operación XOR entre dos imágenes y guarda el resultado.
    
    Args:
        image1_path (str): Ruta de la imagen original
        image2_path (str): Ruta de la imagen llave
        output_path (str): Ruta donde se guardará la imagen resultante
    """
    # Cargar las imágenes
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)
    
    # Convertir a RGB si están en otro modo
    img1 = img1.convert('RGB')
    img2 = img2.convert('RGB')
    
    # Asegurar que ambas imágenes tengan el mismo tamaño
    width = min(img1.size[0], img2.size[0])
    height = min(img1.size[1], img2.size[1])
    
    img1 = img1.resize((width, height))
    img2 = img2.resize((width, height))
    
    # Convertir las imágenes a arrays de NumPy
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    
    # Aplicar XOR
    xor_result = np.bitwise_xor(arr1, arr2)
    
    # Convertir el resultado de vuelta a una imagen
    result_image = Image.fromarray(xor_result)
    
    # Guardar la imagen resultante
    result_image.save(output_path)
    
    return result_image

# Ejemplo de uso
if __name__ == "__main__":
    # Reemplazar con las rutas de tus imágenes
    imagen_original = "./images/Blink-182.jpg"
    imagen_llave = "./images/AM-ArcticMonkeys.jpg"
    imagen_resultado = "./images/resultado_merge_xor.jpg"
    
    resultado = apply_image_xor(imagen_original, imagen_llave, imagen_resultado)
    resultado.show()  # Mostrar la imagen resultante