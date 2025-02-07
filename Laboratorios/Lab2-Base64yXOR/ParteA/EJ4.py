from Utils import utils
def main():
    print("Conversor de Base64 a ASCII (paso a paso)")
    texto_base64 = "SG9sYQ=="
    
    utils.printBase64_to_ascii(texto_base64)

    texto_base64 = "SGVsbG8hIQ=="
    
    utils.printBase64_to_ascii(texto_base64)
    

if __name__ == "__main__":
    main()