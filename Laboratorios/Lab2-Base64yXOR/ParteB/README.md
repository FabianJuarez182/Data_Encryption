# *Lab2 ParteB*
**Por qué al aplicar XOR con una llave de texto la imagén se corrompe?**

Al aplicar XOR con una llave de texto a una imagen, esta se corrompe porque la operación XOR se realiza byte por byte, y los bytes de un archivo de texto (ASCII/UTF-8) tienen un rango limitado , mientras que los bytes de una imagen pueden tener cualquier valor en el rango 0-255. Esta diferencia en los rangos de valores altera la estructura de los datos de la imagen, corrompiendo su formato. También que al no tener formatos iguales y realizar un cambio de la imagen puede que sea imposible de abrir por la estructura que tiene png que no va del todo específica.

**Incovenientes al momento de realizar xor en imagenes**

Al llevar a cabo en realizar el xor entre 2 imagenes es de tener en cuenta el formato y las dimensiones que tiene cada archivo ya que esto puede corromper la imagen. También que los colores pueden venir de formatos distintos y deben de adaptarse para que se tengan el mismo formato ambas imagenes y no tener problemas de formar una imagen final corrupta.