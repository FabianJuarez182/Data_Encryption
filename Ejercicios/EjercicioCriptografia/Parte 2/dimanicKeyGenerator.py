class GeneradorLlaves:
    def generar_llave(self, longitud, palabra_clave):
        """Genera una llave usando una palabra clave que se repite"""
        caracteres = []
        decimales = []
        
        # Convertir la palabra clave a una lista de valores ASCII
        valores_clave = [ord(c) for c in palabra_clave]
        longitud_clave = len(valores_clave)
        
        for i in range(longitud):
            # Usar el valor ASCII del carácter correspondiente de la palabra clave
            valor_decimal = valores_clave[i % longitud_clave]
            caracter = chr(valor_decimal)
            
            caracteres.append(caracter)
            decimales.append(valor_decimal)
        
        return  ''.join(caracteres)
    
def main():
    generador = GeneradorLlaves()
    
    print("Generador de Llaves Dinámicas")
    print("=" * 30)
    
    while True:
        try:
            longitud = int(input("\nIngrese la longitud de la llave deseada: "))
            if longitud <= 0:
                print("La longitud debe ser un número positivo.")
                continue
            
            palabra_clave = input("Ingrese la palabra clave: ")
            if not palabra_clave:
                print("La palabra clave no puede estar vacía.")
                continue
                
            # Generar la llave con la palabra clave
            info_llave = generador.generar_llave(longitud, palabra_clave)
            
            # Mostrar resultados
            print("\nLlave generada:")
            print(f"Caracteres: {info_llave}")
            
            # Preguntar si desea generar otra llave
            continuar = input("\n¿Desea generar otra llave? (s/n): ").lower()
            if continuar != 's':
                break
                
        except ValueError:
            print("Por favor, ingrese un número válido.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()