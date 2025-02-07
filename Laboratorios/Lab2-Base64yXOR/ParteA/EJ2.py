from Utils import utils

def main():
    texto_binario = "01001000 01101111 01101100 01100001"
    
    # Convertir binario a ASCII
    resultado = utils.binario_a_ascii(texto_binario)
    print(f"\nBinario: {texto_binario}")
    print(f"\nBinario a ASCII: {resultado}")

    texto_binario = "01001000 01100101 01101100 01101100 01101111 00100001 00100001"
    
    # Convertir binario a ASCII
    resultado = utils.binario_a_ascii(texto_binario)
    print(f"\nBinario: {texto_binario}")
    print(f"\nBinario a ASCII: {resultado}\n")

if __name__ == "__main__":
    main()