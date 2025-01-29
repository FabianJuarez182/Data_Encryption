class CifradoXOR:
    def texto_a_binario(self, texto):
        """Convierte texto a su representación binaria"""
        return ''.join(format(ord(char), '08b') for char in texto)
    
    def binario_a_texto(self, binario):
        """Convierte una cadena binaria a texto"""
        bytes_lista = [binario[i:i+8] for i in range(0, len(binario), 8)]
        return ''.join(chr(int(byte, 2)) for byte in bytes_lista)
    
    def xor_binario(self, bin1, bin2):
        """Realiza XOR bit a bit entre dos cadenas binarias"""
        resultado = ''
        for b1, b2 in zip(bin1, bin2):
            resultado += '1' if b1 != b2 else '0'
        return resultado
    
    def ajustar_llave(self, llave, longitud_objetivo):
        """Ajusta la llave para que coincida con la longitud objetivo"""
        if len(llave) >= longitud_objetivo:
            return llave[:longitud_objetivo]
        else:
            # Repetir la llave hasta alcanzar la longitud deseada
            llave_repetida = llave * (longitud_objetivo // len(llave) + 1)
            return llave_repetida[:longitud_objetivo]
    
    def cifrar(self, mensaje, llave):
        """Cifra el mensaje usando XOR con la llave ajustada"""
        # Ajustar la llave a la longitud del mensaje
        llave_ajustada = self.ajustar_llave(llave, len(mensaje))
        
        # Convertir mensaje y llave a binario
        mensaje_bin = self.texto_a_binario(mensaje)
        llave_bin = self.texto_a_binario(llave_ajustada)
        
        # Realizar XOR
        resultado_bin = self.xor_binario(mensaje_bin, llave_bin)
        
        return self.binario_a_texto(resultado_bin)

def main():
    cifrador = CifradoXOR()
    
    print("Cypher ASCII con llave dinámica")
    print("=" * 30)
    
    while True:
        try:
            # Obtener mensaje y llave
            mensaje = input("\nIngrese el mensaje a cifrar: ")
            llave = input("Ingrese la llave (se ajustará automáticamente): ")
            
            if not mensaje or not llave:
                print("ERROR: El mensaje y la llave no pueden estar vacíos")
                continue
            
            # Realizar cifrado con la llave ajustada
            llave_ajustada = cifrador.ajustar_llave(llave, len(mensaje))
            texto_cifrado = cifrador.cifrar(mensaje, llave)
            
            # Mostrar resultados
            print("\nResultados:")
            print(f"Mensaje original: {mensaje}")
            print(f"Llave original: {llave}")
            print(f"Llave ajustada: {llave_ajustada}")
            print(f"Mensaje cifrado (ASCII): {texto_cifrado}")
            
            # Mostrar valores binarios para verificación
            print("\nValores binarios:")
            print(f"Mensaje en binario: {cifrador.texto_a_binario(mensaje)}")
            print(f"Llave ajustada en binario: {cifrador.texto_a_binario(llave_ajustada)}")
            print(f"Cifrado en binario: {cifrador.texto_a_binario(texto_cifrado)}")
            
            continuar = input("\n¿Desea cifrar otro mensaje? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()