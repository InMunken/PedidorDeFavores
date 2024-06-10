# Pedidor de Favores

Este software está pensado para resolver el siguiente ejercico encontrado en el [pdf](http://campusvirtual.uno.edu.ar/moodle/pluginfile.php/159506/mod_resource/content/2/TP%202.docx.pdf) de la prácita de programación orientada a objetos II  de la Universidad Nacional del Oeste.

## Estructura del proyecto 
jaja vamos viendo

## Uso del software 
1. Se creará el archivo de entrada.
2. Se ejecutará el archivo `main.py`.
3. Se ingresarán _por consola?_ dos nombres de nodos.

Entonces el programa revolverá cuál es el camino más óptimo para pedir un favor a travez de tus conocidos y los conovidos de sus conocidos.


## Estrucutura del archivo de entrada: 

El archivo de entrada se compondrá de las siguientes partes

- Una línea con N nodos, A, aristas. 
- N líneas que tendrán el nombre de cada nodo.
- A líneas que tendrán las relaciones entre los nodos.


Ejemplo: 
```
4   
Pitusas
Ñandú
InMunken
Pola
Pitusas InMunken AmigoPersonal 
Ñandú Pola Compañero
InMunken Ñandú AmigoPersonal 
InMunken Pola Compañero
Pitusas Pola Conocido
```
