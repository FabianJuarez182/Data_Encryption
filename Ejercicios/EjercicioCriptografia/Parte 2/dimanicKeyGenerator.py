class GeneradorLlaves:
    def __init__(self):
        # Rango de caracteres ASCII imprimibles (32-126)
        self.ascii_min = 32  # espacio
        self.ascii_max = 126 # ~
        self.semilla = 1
    
    def siguiente_numero(self):
        """Genera un número pseudoaleatorio usando el método congruencial lineal"""
        a = 1597
        c = 51749
        m = 244944
        self.semilla = (a * self.semilla + c) % m
        return self.semilla
    
    def generar_ascii_aleatorio(self):
        """Genera un valor ASCII aleatorio dentro del rango válido"""
        rango = self.ascii_max - self.ascii_min + 1
        numero = self.siguiente_numero() % rango
        return self.ascii_min + numero
    
    def generar_llave(self, longitud):
        """Genera una llave de la longitud especificada"""
        caracteres = []
        decimales = []
        
        # Usar el tamaño de la llave como parte de la semilla
        self.semilla = longitud * 1000 + 7
        
        for _ in range(longitud):
            valor_decimal = self.generar_ascii_aleatorio()
            caracter = chr(valor_decimal)
            
            caracteres.append(caracter)
            decimales.append(valor_decimal)
        
        return {
            'llave': ''.join(caracteres),
            'decimales': decimales
        }
    
    def mostrar_detalles_llave(self, info_llave):
        """Muestra los detalles de la llave generada"""
        print("\nDetalles de la llave generada:")
        print("-" * 50)
        print(f"Llave: {info_llave['llave']}")
        print("\nAnálisis por carácter:")
        print("-" * 50)
        print("Posición | Carácter | ASCII")
        print("-" * 50)
        
        for i, (char, decimal) in enumerate(zip(info_llave['llave'], info_llave['decimales'])):
            print(f"{i+1:^8} | {char:^8} | {decimal:^5}")
        
        # Mostrar la llave final en valores ASCII
        print("\nLlave en valores ASCII:")
        print(''.join(str(decimal) for decimal in info_llave['decimales']))

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
                
            # Generar la llave
            info_llave = generador.generar_llave(longitud)
            
            # Mostrar los detalles
            generador.mostrar_detalles_llave(info_llave)
            
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