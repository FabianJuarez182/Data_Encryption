from Utils import utils
def main():
    cifrador = utils.CifradoXOR()
    
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
            print(f"Mensaje en binario: {cifrador.texto_a_binario(mensaje)}")
            print(f"Llave ajustada: {llave_ajustada}")
            print(f"Llave ajustada en binario: {cifrador.texto_a_binario(llave_ajustada)}")
            print(f"Mensaje cifrado (ASCII): {texto_cifrado}")
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