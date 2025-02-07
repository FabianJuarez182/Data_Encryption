from Utils import utils


def main():
    
    # Entrada del usuario
    texto = "Hola"
    
    # Convertir texto
    ascii_binarios, binario_completo = utils.ascii_a_binario(texto)
    
    # Convertir binario a Base64
    resultado_base64 = utils.binario_a_base64(binario_completo)
    
    # Mostrar resultados
    print(f"Texto original: {texto}")
    print(f"Binario: {binario_completo}")
    print(f"Base64: {resultado_base64}")

        # Entrada del usuario
    texto = "Hello!!"
    
    # Convertir texto
    ascii_binarios, binario_completo = utils.ascii_a_binario(texto)
    
    # Convertir binario a Base64
    resultado_base64 = utils.binario_a_base64(binario_completo)
    
    # Mostrar resultados
    print(f"Texto original: {texto}")
    print(f"Binario: {binario_completo}")
    print(f"Base64: {resultado_base64}")


if __name__ == "__main__":
    main()