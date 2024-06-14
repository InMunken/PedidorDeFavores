# Pedidor de Favores

Este software está pensado para resolver el siguiente ejercico encontrado en el [pdf](http://campusvirtual.uno.edu.ar/moodle/pluginfile.php/159506/mod_resource/content/2/TP%202.docx.pdf) de la prácita de programación orientada a objetos II  de la Universidad Nacional del Oeste.

## Estructura del proyecto 
La estructura del proyecto esta definida en `DatosDelProyecto/Diagrama POO2.drawio` y explicada detalladamente en `explicación.txt`.

## Uso del software 
1. Se creará el archivo de entrada.
2. Se ejecutará el archivo `main.py`.
3. Se ingresarán por consola dos nombres de nodos.

Entonces el programa revolverá cuál es el camino "más óptimo" para pedir un favor a través de tus conocidos y los conocidos de sus conocidos. 


## Estrucutura del archivo de entrada: 

El archivo de entrada se compondrá de las siguientes partes

- Una línea con N nodos, A, aristas. 
- N líneas que tendrán el nombre de cada nodo.
- A líneas que tendrán las relaciones entre los nodos.


Ejemplo: 
```
4
Tobias
Ñandú
Federico
Maxi
Tobias Federico AmigoPersonal 
Ñandú Maxi Compañero
Federico Ñandú AmigoPersonal 
Federico Maxi Compañero
Tobias Maxi Conocido
```
