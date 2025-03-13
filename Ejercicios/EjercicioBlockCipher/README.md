# Ejercicio de Block Cipher 

## 📜 Descripción
El ejercicio busca que comprendas los modos de operación en cifrados de bloque y cómo afectan la seguridad y apariencia de los datos cifrados.

## ✨ Características
- Implementación de DES Cipher
- Implementación de 3 DES Cipher
- Implementación de AES Cipher

## 📦 Dependencias Principales
Las principales dependencias del proyecto incluyen:
* [![Python][Python]][Python-url]
* [![Markdown][Markdown]][Markdown-url]

## 👥 Developer

* [![Linkedin][Linkedin]][Linkedin-fabian]
* [![GitHub][GitHub]][GitHub-fabian]

## 📖 Ejercicios
### Uso del programa
```bash
python CifradoDecifradoKeystream.py 
```
Por defecto poseemos un caso, si se desea probar otro modificar la información del ejercicio

### Uso de tests
```bash
python -m unittest Test.py
```

## Ejemplos de uso

### Ejemplo Cipher DES

Input:
```bash
Texto original:  The DES block cipher is a 16-round Feistel network with a block length of\n64 bits and a key length of 56 bits. The same round function \xcb\x86 f is used in each\nof the 16 rounds. The round function takes a 48-bit sub-key and, as expected\nfor a (balanced) Feistel network, a 32-bit input (namely, half a block). The\nkey schedule of DES is used to derive a sequence of 48-bit sub-keys k1, . . . , k16\nfrom the 56-bit master key.             
```
Output:
```bash
Clave: 5bb2a743c4f0a90c
Texto cifrado: 94cf615b9088fe4b8e2deb6bcdea92d41002011babcf67568912c866eba06b6ae25b682dd0ca930103aca871bd1115b90d6582bcb79f03f94bfc34a9e1ff85450fc155939d8480ffba6460275133a7d9610b9d85344a1d255865e00af821848aa5c78e3068170086f453d10b70243532de31f7a7bbfc9c00232103b0523a25387e475e2ba937e57b70c11a5b27544d5a2fcae09e7764615da5f49b06e7ed7ce69a32ba52cba44a7a98db3a633ab3e5b220c1279f5519f065ffe99bb4dc0dca421dc3f53ef57717113553b35786dd78e44eac7ca80f0f28e563afab102ac9d4886c4e5163474e189f92d6c3603b6b5906e9a47c958de7b569d9827712eb7952a8ab731e08099ebb7513780d05bbe41e371b1ed3b6e6848cf890e6d3e051163352061d48c0d8f4081288969e4fe75b570c89d849fb8aac78a2f1b4a084c9479afa3be4bc13c7991e38d2747202df4f67a122c1cc274ab02d8e20c70ab3c77fae9e5fed954293dd5b22720df723735382b92a76c2ce0d8978ac1756d2ad0998b2ef93735d792d210c3e57f20980cafc08a2389203c08c487a75ba36eb09e8e20c9d7d72cbc0e0e5b858   
```

### Ejemplo Cipher 3DES

Input:
```bash
Mensaje cifrado: \xe0*\x82@-\xf3\xe5\xc8\xe1\x15T\xdf\x92\x0b\xa9hZ\xda\xcc\'\x16S\xa5m-\xdb\xdf\x81.\xce}\xab\xd1\xab\xc6\xba\n9\xc6\x10s\x94Iy6\xfc3\xa0O\xc5\xcb^\xe14& 6\xdb\x86-\x898\xf2>\xfa\xaa\x0c\x9d09\x08\x15E\xeb\xc14\xc0\x12[s\x99=\xb8\x981\x8f\x10\xdb\x82\x1e\x86\xe2\x7f,\xb9\xb1\x1el\xe4\x9d\xd6\x1c\xef@6\x06\xad\xe5J\x15O\xd1h\x88\xc8\xf5,x\r\xaa;J\xc2\xb7\x82\xf2,v\xf5\x99L\x14`\xe4\x15\x92|8\xc6\x0c\xd3f\xe8y\xabR3\xfeou0\xe6P\xfex2?\xe8\x05\xf0\xb6\xda\xc6\x17\x0f\xd1\x10&!"\xec\xb1\x82\x86\x1a\xed\x140\xd4\xf4+\xae\x12GE\xda\x06;\xf9\x8b\xbdAi\x8ec(z\x8dh\xe9\x0bGY\x89i\xef8z\xbd\xee\xfd\xf4\xda\x88\x01%\xb4\x06\x04\x86\xb6\xcd\x1f\xfa\xcc\x1fB\xe4R\x9cw\x82\x01F\xea[\x87|\xab\x7fL\x0c\\\x9b\xd3\xe4zl\x90\x82\xab\x02\xb4\x98Q\x0c2\xb9w\x18R.\xb3\xb6B\xff\x96\xd1tT\xfa\x1e\x8b\xef\x12!\x05b\xe2Y\x97\xf8\x0fdJ@o\x80:\xe1\x0f\x98G^P\xfc\xb7J\xe1\x9fP\x89)dI\xe0M\xca\x00\x96\xda\x06$\xbb\xf6\xe2\xca\x89\x95\xab1\x19qg\xa3,H4\xc2j\xb9=c\xe7\x8b2k\xe2\x91i\x85\xf9\x82\xb0\x96\xe88\xbcS\xcf\xc7\x19#\xe3k\xfc\x00\x135\x82\xb3\xa8\xfa\xa2!8$\x05\xc7\x04\xd7m\xb3/\xe5\x97!\xa7\x8d\x01\xea\xde\x96\xfc}<\x83\xa8\xe1\xacP\x9d\xff\xb8v\xc2\xd9?\xdc4x\xd5C1\xf4d\x84\xceV\xde\xd1K\xe0\x1c\xdd\x92\xa4_1\xe7\xc3\xfe\xee\xa2o\xd2X\xaa\x87\xf5N\xca                   
```
Output:
```bash
Mensaje descifrado: The main weakness of DES is its short key. It thus makes sense to try to
design a block cipher with a larger key length using DES as a building block.
Some approaches to doing so are discussed in this section. Although we refer
to DES frequently throughout the discussion, and DES is the most prominent
block cipher to which these techniques have been applied, everything we say
here applies generically to any block cipher.  
```

### Ejemplo Ejercicio Cipher AES con Imagenes
Imagen Original:
![alt text](pic.png)

Cifrado ECB
![alt text](encrypted_ecb_image.png)

Cifrado CBC
![alt text](encrypted_cbc_image.png)

## Preguntas
1. ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
    - DES: Clave de 8 bytes
    - 3DES: Utiliza claves de 24 bytes
    - AES: Utiliza clave de 32 bytes

2. ¿Qué modo de operación está implementado?
    - DES: Utiliza el modo ECB
    - 3DES: Utiliza el modo CBC
    - AES: Utiliza el modo ECB y CBC

3. ¿Por qué no debemos usar ECB en datos sensibles?
    - No se debe utilizar porque no oculta del todo los patrones de datos. Al llevar a cabo un cifrado de bloques identicos de texto plano al cifrado puede revelar informacion de los datos originales como se puede evidanciar en el Ejemplo 3 de las imagenes. Es bastante facil visualizar en las imagenes cifradas o en texto cifrado y se pueden llegar a distinguir patrones y formas con facilidad.

4. ¿Cual es la diferencia entre ECB vs CBC, se puede notar directamente en una imagen?
    - ECB: Cada bloque es cifrado de forma independiente, por lo que los patrones en los datos originales se mantienen visibles tras el cifrado.
    - CBC: Cada bloque cifrado depende del bloque anterior, comenzando con un Vector de Inicialización (IV). Esto oculta patrones y genera imágenes visualmente más "aleatorias".
    - Diferencia visual: En una imagen cifrada con ECB, puedes reconocer contornos y patrones. En cambio, con CBC, la imagen parece ruido estático.

5. ¿Que es el IV?
    Es un valor aleatorio que asignamos, la cual se utiliza junto con la clave para cifrar los datos y añadir aleatoriedad en los cifrados individuales de los bloques.

6. ¿Que es el PADDING?
    Es una técnica que agrega una cantidad de bytes a una cadena para que el algoritmo al ser separado por bloques pueda completar el numero exacto de bloques y no quede incapaz de cifrar.

7. ¿En qué situaciones se recomienda cada modo de operación?
    - CBC: Se recomienda en archivos grandes pero que esten asegurados para no ser propenso a ningun riesgo y siempre usar un IV seguro.
    - ECB: No se recomienda para datos sensibles y de ser usados que no contengan patrones para que no se note el tipo de encripcion.

8. ¿Cómo elegir un modo seguro en cada lenguaje de programación?
    El modo de encripción no varia segun el lenguaje a utilizar. Esto mas depende que es lo que se desea encriptar, dependiendo así de la seguridad y velocidad de encripcion que se tiene en el momento. 

## Referencias
```
Dworkin, M. J. (2001). Recommendation for block cipher modes of operation : https://doi.org/10.6028/nist.sp.800-38a
```


<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.markdownguide.org
[Linkedin-fabian]: https://www.linkedin.com/in/fabianjua/
[Linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Github-fabian]: https://github.com/FabianJuarez182/
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white