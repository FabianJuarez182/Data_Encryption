import unittest
import sys
import os

# Agregar las rutas de los directorios padre y adyacentes al path de Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Utils'))

# Ahora podemos importar los módulos
from Utils.utils import CifradoXOR, bytes_to_hex
from GeneracionKeystream import generate_keystream
from CifradoDecifradoKeystream import CifradoDecifradoKeystream

class TestCifradoKeystream(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para las pruebas"""
        self.cifrador = CifradoXOR()
    
    def test_cifrado_descifrado_basico(self):
        """Prueba básica de cifrado y descifrado con keystream"""
        mensaje = "Hola Mundo"
        clave = "clave_secreta"
        
        # Generar keystream
        keystream = generate_keystream(clave, len(mensaje))
        keystream_text = bytes_to_hex(keystream)
        
        # Ajustar keystream a la longitud del mensaje
        llave_ajustada = self.cifrador.ajustar_llave(keystream_text, len(mensaje))
        
        # Cifrar mensaje
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text)
        
        # Descifrar mensaje
        mensaje_descifrado = self.cifrador.descifrar(texto_cifrado, llave_ajustada)
        
        # Verificar que el mensaje descifrado coincide con el original
        self.assertEqual(mensaje, mensaje_descifrado)
    
    def test_cifrado_descifrado_mensaje_largo(self):
        """Prueba con un mensaje más largo"""
        mensaje = "Este es un mensaje largo para probar que el cifrado y descifrado funcionan correctamente con textos extensos"
        clave = "clave_muy_secreta_2024"
        
        # Generar keystream
        keystream = generate_keystream(clave, len(mensaje))
        keystream_text = bytes_to_hex(keystream)
        
        # Ajustar keystream a la longitud del mensaje
        llave_ajustada = self.cifrador.ajustar_llave(keystream_text, len(mensaje))
        
        # Cifrar mensaje
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text)
        
        # Descifrar mensaje
        mensaje_descifrado = self.cifrador.descifrar(texto_cifrado, llave_ajustada)
        
        # Verificar que el mensaje descifrado coincide con el original
        self.assertEqual(mensaje, mensaje_descifrado)
    
    def test_cifrado_descifrado_caracteres_especiales(self):
        """Prueba con caracteres especiales y símbolos"""
        mensaje = "!@#$%^&*()_+{}[]|:;<>,.?/~`áéíóúÁÉÍÓÚñÑ"
        clave = "clave_2024!@#"
        
        # Generar keystream
        keystream = generate_keystream(clave, len(mensaje))
        keystream_text = bytes_to_hex(keystream)
        
        # Ajustar keystream a la longitud del mensaje
        llave_ajustada = self.cifrador.ajustar_llave(keystream_text, len(mensaje))
        
        # Cifrar mensaje
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text)
        
        # Descifrar mensaje
        mensaje_descifrado = self.cifrador.descifrar(texto_cifrado, llave_ajustada)
        
        # Verificar que el mensaje descifrado coincide con el original
        self.assertEqual(mensaje, mensaje_descifrado)
    
    def test_cifrado_descifrado_claves_diferentes(self):
        """Prueba que el descifrado falla con una clave diferente"""
        mensaje = "Mensaje secreto"
        clave_original = "clave_correcta"
        clave_incorrecta = "clave_incorrecta"
        
        # Generar keystream con clave original
        keystream_original = generate_keystream(clave_original, len(mensaje))
        keystream_text_original = bytes_to_hex(keystream_original)
        
        # Generar keystream con clave incorrecta
        keystream_incorrecto = generate_keystream(clave_incorrecta, len(mensaje))
        keystream_text_incorrecto = bytes_to_hex(keystream_incorrecto)
        
        # Ajustar keystreams
        llave_ajustada_original = self.cifrador.ajustar_llave(keystream_text_original, len(mensaje))
        llave_ajustada_incorrecta = self.cifrador.ajustar_llave(keystream_text_incorrecto, len(mensaje))
        
        # Cifrar con la clave original
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text_original)
        
        # Descifrar con la clave incorrecta
        mensaje_descifrado_incorrecto = self.cifrador.descifrar(texto_cifrado, llave_ajustada_incorrecta)
        
        # Verificar que el descifrado con clave incorrecta no coincide con el mensaje original
        self.assertNotEqual(mensaje, mensaje_descifrado_incorrecto)
        
        # Descifrar con la clave correcta
        mensaje_descifrado_correcto = self.cifrador.descifrar(texto_cifrado, llave_ajustada_original)
        
        # Verificar que el descifrado con clave correcta coincide con el mensaje original
        self.assertEqual(mensaje, mensaje_descifrado_correcto)
    
    def test_cifrado_descifrado_mismo_keystream(self):
        """Prueba que se utiliza el mismo keystream para cifrar y descifrar"""
        mensaje = "Texto de prueba"
        clave = "mi_clave"
        
        # Generar keystream
        keystream = generate_keystream(clave, len(mensaje))
        keystream_text = bytes_to_hex(keystream)
        
        # Generar un segundo keystream idéntico para verificar
        keystream2 = generate_keystream(clave, len(mensaje))
        keystream_text2 = bytes_to_hex(keystream2)
        
        # Verificar que ambos keystreams son idénticos para la misma clave y longitud
        self.assertEqual(keystream_text, keystream_text2)
        
        # Ajustar keystream
        llave_ajustada = self.cifrador.ajustar_llave(keystream_text, len(mensaje))
        
        # Cifrar mensaje
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text)
        
        # Descifrar mensaje
        mensaje_descifrado = self.cifrador.descifrar(texto_cifrado, llave_ajustada)
        
        # Verificar que el mensaje descifrado coincide con el original
        self.assertEqual(mensaje, mensaje_descifrado)
    
    def test_operacion_xor_simetrica(self):
        """Prueba que la operación XOR es simétrica"""
        mensaje = "Texto prueba XOR"
        clave = "clave_xor"
        
        # Generar keystream
        keystream = generate_keystream(clave, len(mensaje))
        keystream_text = bytes_to_hex(keystream)
        
        # Ajustar keystream
        llave_ajustada = self.cifrador.ajustar_llave(keystream_text, len(mensaje))
        
        # Cifrar mensaje
        texto_cifrado = self.cifrador.cifrar(mensaje, keystream_text)
        
        # Cifrar el texto cifrado de nuevo con la misma clave
        texto_recifrado = self.cifrador.cifrar(texto_cifrado, llave_ajustada)
        
        # Verificar que el texto recifrado es igual al mensaje original
        # Esto demuestra la propiedad simétrica de XOR (A ⊕ B ⊕ B = A)
        self.assertEqual(mensaje, texto_recifrado)

if __name__ == '__main__':
    unittest.main()