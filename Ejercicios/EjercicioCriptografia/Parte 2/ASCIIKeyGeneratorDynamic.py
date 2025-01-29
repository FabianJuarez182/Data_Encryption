class GeneradorLlave:
    def generar_numero_pseudo_aleatorio(self, semilla, min_valor, max_valor):
        """Genera un número pseudo aleatorio usando un algoritmo simple"""
        a = 1664525
        c = 1013904223
        m = 2**32
        semilla = (a * semilla + c) % m
        return min_valor + (semilla % (max_valor - min_valor + 1)), semilla

    def generar_llave(self, longitud, semilla_inicial=123456789):
        """Genera una llave aleatoria de la longitud especificada"""
        llave = []
        semilla = semilla_inicial
        
        for _ in range(longitud):
            numero, semilla = self.generar_numero_pseudo_aleatorio(semilla, 32, 126)
            llave.append(chr(numero))
            
        return ''.join(llave)

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
            # Repetir la llave hasta alcanzar o superar la longitud objetivo
            repeticiones = (longitud_objetivo + len(llave) - 1) // len(llave)
            return (llave * repeticiones)[:longitud_objetivo]
    
    def cifrar(self, mensaje, llave):
        """Cifra el mensaje usando XOR con la llave ajustada"""
        # Ajustar la llave si es necesario
        llave_ajustada = self.ajustar_llave(llave, len(mensaje))
        
        # Convertir a binario y realizar XOR
        mensaje_bin = self.texto_a_binario(mensaje)
        llave_bin = self.texto_a_binario(llave_ajustada)
        resultado_bin = self.xor_binario(mensaje_bin, llave_bin)
        
        return self.binario_a_texto(resultado_bin)

def main():
    generador = GeneradorLlave()
    cifrador = CifradoXOR()
    
    print("Cifrado con Llave Dinamica")
    print("=" * 30)
    
    while True:
        try:
            # Obtener mensaje primero
            mensaje = input("\nIngrese el mensaje a cifrar: ")
            if not mensaje:
                print("ERROR: El mensaje no puede estar vacío")
                continue
            
            # Obtener longitud de llave deseada
            longitud_llave = int(input("Ingrese la longitud de la llave a generar: "))
            if longitud_llave <= 0:
                print("ERROR: La longitud debe ser un número positivo")
                continue
            
            # Generar llave aleatoria inicial
            llave_inicial = generador.generar_llave(longitud_llave)
            
            # Ajustar la llave al tamaño del mensaje
            llave_ajustada = cifrador.ajustar_llave(llave_inicial, len(mensaje))
            
            # Realizar cifrado
            texto_cifrado = cifrador.cifrar(mensaje, llave_inicial)
            
            # Mostrar resultados
            print("\nResultados:")
            print(f"Mensaje original: {mensaje}")
            print(f"Longitud del mensaje: {len(mensaje)}")
            print(f"Llave generada original: {llave_inicial}")
            print(f"Longitud de llave original: {len(llave_inicial)}")
            print(f"Llave ajustada: {llave_ajustada}")
            print(f"Longitud de llave ajustada: {len(llave_ajustada)}")
            print(f"Mensaje cifrado (ASCII): {texto_cifrado}")
            
            # Mostrar valores binarios para verificación
            print("\nValores binarios:")
            print(f"Mensaje en binario: {cifrador.texto_a_binario(mensaje)}")
            print(f"Llave ajustada en binario: {cifrador.texto_a_binario(llave_ajustada)}")
            print(f"Cifrado en binario: {cifrador.texto_a_binario(texto_cifrado)}")
            
            # Verificación de descifrado
            mensaje_descifrado = cifrador.cifrar(texto_cifrado, llave_inicial)
            print(f"\nMensaje descifrado: {mensaje_descifrado}")
            
            continuar = input("\n¿Desea cifrar otro mensaje? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError as e:
            print(f"Error: Ingrese un número válido para la longitud")
        except Exception as e:
            print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()