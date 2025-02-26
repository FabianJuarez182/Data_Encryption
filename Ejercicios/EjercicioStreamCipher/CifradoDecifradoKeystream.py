from Utils import utils
from GeneracionKeystream import generate_keystream

def CifradoDecifradoKeystream(mensaje, clave):
    cifrador = utils.CifradoXOR()
    
    print("Cifrado de Keystream y Decifrado con llave dinámica")
    print("=" * 30)
    
    # Generamos el keystream
    keystream = generate_keystream(clave, len(mensaje))
    
    keystream_text = utils.bytes_to_hex(keystream)
    # Realizar cifrado con la llave ajustada
    texto_cifrado = cifrador.cifrar(mensaje, keystream_text)
    
    # Mostrar resultados Cifrados
    print("\nResultados:")
    print(f"Mensaje original: {mensaje}")
    print(f"Mensaje en binario: {cifrador.texto_a_binario(mensaje)}")
    print(f"Llave : {keystream_text}")
    print(f"Mensaje cifrado (ASCII): {texto_cifrado}")
    print(f"Cifrado en binario: {cifrador.texto_a_binario(texto_cifrado)}")
    
    # Mostrar resultados Descifrar
    mensaje_descifrado = cifrador.descifrar(texto_cifrado, keystream_text)
    print("\nResultados Descifrado:")
    print(f"Mensaje cifrado (ASCII): {texto_cifrado}")
    print(f"Mensaje descifrado (ASCII): {mensaje_descifrado}")


def main():
    CifradoDecifradoKeystream("Este es un mensaje secreto", "mi_clave_secreta_2024")

if __name__ == "__main__":
    main()