# Proyecto 1: Animando Estructuras de Datos - Binary Search Tree (BST)

**Curso:** CS2023 Algoritmos y Estructuras de Datos  
**Institución:** Universidad de Ingeniería y Tecnología (UTEC)

## Autores
* Jorge Andres Cuevas Sanchez
* Italo Stefano Mendez Haro
* Nicolas Fabian Trillo Ñahui

## Descripción del Proyecto
Este repositorio contiene una animación interactiva y educativa desarrollada con Manim (Community Edition) en Python. El video final demuestra de manera visual y didáctica el funcionamiento de un **Binary Search Tree (BST)**, cumpliendo con los requisitos del proyecto y detallando paso a paso las operaciones fundamentales de la estructura.

Como característica especial, la animación incluye una narración por voz generada con inteligencia artificial, sincronizada con cada operación mostrada para guiar al espectador a través de los siguientes conceptos:

* **Definición Teórica:** Propiedad fundamental del árbol donde el subárbol izquierdo es menor a la raíz y el derecho es mayor.
* **Inserción (Insert):** Descenso recursivo por el árbol e inserción de la clave `25` asumiendo la posición de nodo hoja.
* **Búsqueda (Search):** Recorrido condicional para encontrar la clave `40` descartando ramas innecesarias.
* **Eliminación (Remove):** Resolución del Caso 1 (Nodo Hoja) liberando memoria y anulando el puntero del padre para la clave `40`.
* **Recorridos DFS (Tree Traversals):** Ejecución sistemática de In-order, Pre-order y Post-order.

## Descripción de la Estructura de Datos
Un Binary Search Tree (BST) es un árbol binario (grafo conexo acíclico con raíz) estructurado jerárquicamente donde cada nodo almacena una clave y cumple con una propiedad estricta de ordenamiento:

* Todos los elementos ubicados en el subárbol izquierdo de un nodo tienen un valor estrictamente menor que él.
* Todos los elementos ubicados en el subárbol derecho de un nodo tienen un valor estrictamente mayor que él.

Esta estructura permite optimizar los tiempos de ejecución de las operaciones básicas.

### Análisis de Complejidad
La eficiencia de un BST está directamente ligada a su altura ($h$).

* **Caso Promedio (Árbol Balanceado):** Al descartar la mitad del árbol en cada decisión, las operaciones de búsqueda, inserción y eliminación toman un tiempo de $O(\log n)$.
* **Peor Caso (Árbol Degenerado/Skewed):** Si los elementos se insertan en un orden puramente ascendente o descendente, el árbol adquiere una forma lineal (funcionalmente idéntica a una Linked List). En este escenario, la altura se vuelve $h=n-1$ y las operaciones se degradan a un tiempo de $O(n)$.

## Software Requerido
* **Python:** 3.9 o superior (compatible con entornos 3.9 de macOS y 3.14 de Windows).
* **Bibliotecas de Python:** `manim` e `importlib-metadata` (esta última necesaria para versiones anteriores a Python 3.10).
* **Dependencias del Sistema:** 
  * FFmpeg (Obligatorio para la codificación del video final en formato MPEG).
  * Microsoft C++ Build Tools (Solo necesario en Windows para la compilación de dependencias gráficas).

## Cómo Compilar y Ejecutar

> [!WARNING]
> **IMPORTANTE:** No ejecutes el archivo utilizando el botón tradicional "Run Python File" del editor. La escena debe renderizarse estrictamente mediante los comandos de terminal de Manim. Además, **no separes el archivo `main.py` de la carpeta `audio`**, ya que el código depende de esos recursos para la narración.

Para generar la animación, abre la terminal en la raíz de este proyecto y ejecuta los siguientes comandos según la calidad deseada:

**Previsualización rápida (Baja calidad para pruebas):**
```bash
python -m manim -pql main.py AnimacionBST
```

**Video Final (Alta resolución 1080p a 60fps):**
```bash
python -m manim -pqh main.py AnimacionBST
```
