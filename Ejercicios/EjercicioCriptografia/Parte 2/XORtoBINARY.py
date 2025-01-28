
def validar_binario(binario):
    # Eliminar espacios si existen
    binario = binario.replace(" ", "")
    
    # Verificar que solo contenga 0s y 1s
    if not all(bit in '01' for bit in binario):
        raise ValueError("El texto debe contener solo 0s y 1s")
    
    return binario

def igualar_longitud(bin1, bin2):
    # Encontrar la longitud máxima
    max_len = max(len(bin1), len(bin2))
    
    # Rellenar con ceros a la izquierda si es necesario
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    return bin1, bin2

def aplicar_xor(bin1, bin2):
    try:
        # Validar y limpiar las entradas
        bin1 = validar_binario(bin1)
        bin2 = validar_binario(bin2)
        
        # Igualar longitudes
        bin1, bin2 = igualar_longitud(bin1, bin2)
        
        # Lista para almacenar el resultado
        resultado = []
        
        # Aplicar XOR bit a bit
        for b1, b2 in zip(bin1, bin2):
            # XOR: 1 si los bits son diferentes, 0 si son iguales
            xor_bit = '1' if b1 != b2 else '0'
            resultado.append(xor_bit)
        
        # Convertir a string y agrupar en bytes (8 bits)
        resultado_str = ''.join(resultado)
        resultado_agrupado = ' '.join(resultado_str[i:i+8] 
                                    for i in range(0, len(resultado_str), 8))
        
        return resultado_agrupado
        
    except ValueError as e:
        return f"Error: {str(e)}"

def main():
    print("Aplicación de XOR a números binarios")
    
    bin1 = "01001000 01100101"
    bin2 = "11110000 00001111"
    
    resultado = aplicar_xor(bin1, bin2)
    
    print("\nOperación XOR:")
    print(f"Binario 1: {bin1}")
    print(f"Binario 2: {bin2}")
    print(f"Resultado: {resultado}")
    
    # Mostrar tabla de comparación
    print("\nComparación bit a bit:")
    print("Bin1 | Bin2 | XOR")
    print("-" * 20)
    
    bin1_clean = bin1.replace(" ", "")
    bin2_clean = bin2.replace(" ", "")
    resultado_clean = resultado.replace(" ", "")
    
    for b1, b2, r in zip(bin1_clean, bin2_clean, resultado_clean):
        print(f"  {b1}  |  {b2}   |  {r}")

if __name__ == "__main__":
    main()