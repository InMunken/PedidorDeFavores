# Pedidor de Favores

Este software está pensado para resolver el siguiente ejercico encontrado en el [pdf](http://campusvirtual.uno.edu.ar/moodle/pluginfile.php/159506/mod_resource/content/2/TP%202.docx.pdf) de la prácita de programación orientada a objetos II  de la Universidad Nacional del Oeste.

## Estructura del proyecto 
jaja vamos viendo

## Uso del software 
1. Se modifican los parámetros internos del código.
2. Se ejecutará el archivo `reducido.py`.
3. Se ingresarán _por consola?_ dos nombres de nodos.

Entonces el programa revolverá "cuál es el camino más óptimo" para pedir un favor a travez de tus conocidos y los conovidos de sus conocidos.


## Estrucutura del código de entrada: 

Se creará un diccionario `grafo` y se llenará con la función `agregar_relacion` espeficando que será al grafo, nombre del nodo, nombre del nodo conectado y tipo de relación.


Ejemplo: 
```
grafo = {}
agregar_relacion(grafo, "Juan", "Pedro", "amigo personal")
agregar_relacion(grafo, "Pedro", "María", "compañero")
agregar_relacion(grafo, "Juan", "María", "compañero")
```
