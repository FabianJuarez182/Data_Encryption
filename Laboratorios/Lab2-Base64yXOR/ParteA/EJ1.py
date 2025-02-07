from Utils import utils
# Función principal
def main():
    # Entrada del usuario
    texto = "Hola"
    
    # Convertir texto
    ascii_binarios, binario_completo = utils.ascii_a_binario(texto)
    
    utils.imprimir_texto_ascii_bin(texto,ascii_binarios, binario_completo )

    # Entrada del usuario
    texto = "Hello!!"
    
    # Convertir texto
    ascii_binarios, binario_completo = utils.ascii_a_binario(texto)
    
    utils.imprimir_texto_ascii_bin(texto,ascii_binarios, binario_completo )

# Ejecutar el programa
if __name__ == "__main__":
    main()