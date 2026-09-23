# Proyecto 1: Animando Estructuras de Datos - Binary Search Tree (BST)

## Autores
* Jorge Andres Cuevas Sanchez
* Italo Stefano Mendez Haro
* Nicolas Fabian Trillo Ñahui

**Curso:** CS2023 Algoritmos y Estructuras de Datos

## Descripción del Proyecto
Este repositorio contiene una animación interactiva desarrollada con la biblioteca Manim (Community Edition) en Python. El video final demuestra de manera visual y didáctica el funcionamiento de un **Binary Search Tree (BST)**, cumpliendo con los requisitos del proyecto y detallando paso a paso las operaciones fundamentales de la estructura.

Las operaciones y conceptos ilustrados en el video incluyen:
* **Definición Teórica:** Propiedad fundamental del árbol donde el subárbol izquierdo es menor a la raíz y el derecho es mayor.
* **Inserción (Insert):** Descenso recursivo por el árbol e inserción de la clave `25` asumiendo la posición de nodo hoja.
* **Búsqueda (Search):** Recorrido condicional para encontrar la clave `40` descartando ramas innecesarias.
* **Eliminación (Remove):** Resolución del Caso 1 (Nodo Hoja) liberando memoria y anulando el puntero del padre para la clave `40`.
* **Recorridos DFS (Tree Traversals):** Ejecución sistemática de In-order, Pre-order y Post-order.

## Software Requerido
* **Python:** 3.14
* **Biblioteca:** `manim` (v0.21.0)
* **Dependencias del Sistema:** Microsoft C++ Build Tools (para compilación de dependencias gráficas de Python) y FFmpeg (obligatorio para la codificación del video final en formato MPEG).

## Cómo Compilar y Ejecutar
Para generar la animación, abre la terminal en la raíz de este proyecto y ejecuta los siguientes comandos según la calidad deseada:

**Previsualización rápida (Baja calidad para pruebas):**
`manim -pql main.py AnimacionBST`

**Video Final (Alta resolución 1080p a 60fps):**
`manim -pqh main.py AnimacionBST`

*(Nota: El archivo de video generado se guardará automáticamente en el directorio `/media/videos/main/1080p60/`)*

## Descripción de la Estructura de Datos
Un **Binary Search Tree (BST)** es un árbol binario (grafo conexo acíclico con raíz) estructurado jerárquicamente donde cada nodo almacena una clave y cumple con una propiedad estricta de ordenamiento:
* Todos los elementos ubicados en el subárbol izquierdo de un nodo tienen un valor estrictamente menor que él.
* Todos los elementos ubicados en el subárbol derecho de un nodo tienen un valor estrictamente mayor que él.

Esta estructura permite optimizar los tiempos de ejecución de las operaciones básicas. 

### Análisis de Complejidad
La eficiencia de un BST está directamente ligada a su altura ($h$).
* **Caso Promedio (Árbol Balanceado):** Al descartar la mitad del árbol en cada decisión, las operaciones de búsqueda, inserción y eliminación toman un tiempo de $O(\log n)$.
* **Peor Caso (Árbol Degenerado/Skewed):** Si los elementos se insertan en un orden puramente ascendente o descendente, el árbol adquiere una forma lineal (funcionalmente idéntica a una Linked List). En este escenario, la altura se vuelve $h = n - 1$ y las operaciones se degradan a un tiempo de $O(n)$.
