# Ejercicio de Stream Cipher 

## 📜 Descripción
Este ejercicio tiene como objetivo reforzar conocimientos sobre keystram y su importancia en los cifrados de flujo.

## ✨ Características
- Implementación de generador de keystreams
- Implementación de un esquema básico de cifrado y descifrado utilizando XOR
- Análisis de la implicaciones de reutilización del keystream

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

### Ejemplo 1

Input:
```bash
Mensaje: 'Este es un mensaje secreto'
clave: 'mi_clave_secreta_2024'                      
```
Output:
```bash
cyphered text: 'vJ@UUFFY^\YKSJ]EW'
decyphered text: 'Este es un mensaje secreto'
```

### Ejemplo 2

Input:
```bash
Mensaje: '!@#$%^&*()_+{}[]|:;<>,.?/~`áéíóúÁÉÍÓÚñÑ'
clave: 'clave_2024!@#'                      
```
Output:
```bash
cyphered text: '!BBlOIhDcl
              NNSØÜÎø­¨°¼È·'
decyphered text: '!@#$%^&*()_+{}[]|:;<>,.?/~`áéíóúÁÉÍÓÚñÑ'
```

### Ejemplo 3

Input:
```bash
Mensaje: "Perros odian gatos"
clave:  "gufguf"   
```
Output:
```bash
cyphered text: '`]J^JD
[_Z@'
decyphered text: 'Perros odian gatos'
```


## Preguntas
1. ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?
Al modificar la clave con la que se genera el keystream, el mensaje cifrado sera distinto.

2. ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
Si se reutilizará el mismo keystream para dos mensajes diferentes se podria dar una vulnerabilidad de conocer el keystram y poder decifrar
ambos mensajes sin la necesidad de conocer la llave que se utilizo para llevar a cabo dicha llave y conseguir los mensajes cifrados.

3. ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
Entre mayor sea el keystream sera mucho mas robusto y realizar un ataque de fuerza bruta no sera tan facil para conseguir romperlo.

4. ¿Qué consideraciones debes tener al generar un keystream en un entorno real?
Debemos de lograr conseguir aleatoriedad en la generacion del keystream, este debe ser llevado a cabo en lo mas dentro del programa. En este caso este seria el servidor ya que es mas complicado ser comprometido y este está mas resguardado.


5. ¿Qué mejoras ofrecen estos algoritmos frente a un PRNG sencillo? (ChaCha20 y otros)
Los algoritmos modernos de cifrado de flujo ofrecen una serie de mejoras frente a un PRNG sencillo, como:
- Un PRNG sencillo puede tener patrones predecibles, lo que lo hace vulnerable a ataques de predicción.
- Muchos PRNGs sencillos permiten que un atacante, al conocer algunos números generados, reconstruya el estado interno y prediga futuros valores. ChaCha20 evita la transformación que es altamente no lineal
- PRNGs tradicionales tienen periodos relativamente cortos y, a medida que generan más números, pueden exhibir ciclos o repeticiones.

## Referencias
```
Tasker, B. (2020, 20 febrero). Writing (and backdooring) a ChaCha20 based CSPRNG. www.bentasker.co.uk. https://www.bentasker.co.uk/posts/blog/software-development/689-writing-a-chacha20-based-csprng.html
```

## 🤖 Uso de IA
* Se utilizó Claude 3.7 Sonnet. Haz clic [aquí](https://claude.ai/share/118c92d2-1655-4be2-a246-871a88c1670c) para visualizar el chat


<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.markdownguide.org
[Linkedin-fabian]: https://www.linkedin.com/in/fabianjua/
[Linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Github-fabian]: https://github.com/FabianJuarez182/
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white