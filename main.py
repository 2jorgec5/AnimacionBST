from manim import *


class AnimacionBST(Scene):
    def construct(self):
        # --- SECCIÓN 1: TÍTULO Y CRÉDITOS ---
        self.add_sound("audio/01_intro.mp3")
        titulo = Text("Binary Search Tree (BST)", font_size=48, weight=BOLD)
        curso = Text("Algoritmos y Estructuras de Datos", font_size=32)
        autores = Text("Autores:\n- Jorge Andres Cuevas Sanchez\n- Italo Stefano Mendez Haro\n- Nicolas Fabian Trillo Ñahui ",font_size=24, color=GRAY)

        grupo_intro = VGroup(titulo, curso, autores).arrange(DOWN, buff=0.5)

        self.play(Write(titulo, run_time=2))
        self.play(FadeIn(curso, shift=UP, run_time=1.5))
        self.play(FadeIn(autores, run_time=1.5))
        self.wait(11.5)
        self.play(FadeOut(grupo_intro, run_time=1.5))

        # --- SECCIÓN 2: DEFINICIÓN Y PROPIEDADES ---
        self.add_sound("audio/02_definicion.mp3")
        titulo_prop = Text("¿Qué es un Binary Search Tree?", font_size=36).to_edge(UP)
        self.play(Write(titulo_prop, run_time=1.5))

        vertices = [50, 30, 70, 20, 40]
        aristas = [(50, 30), (50, 70), (30, 20), (30, 40)]
        posiciones = {
            50: [0, 2.5, 0],
            30: [-2.5, 0.5, 0],
            70: [2.5, 0.5, 0],
            20: [-4, -1.5, 0],
            40: [-1, -1.5, 0]
        }
        etiquetas = {v: Text(str(v), font_size=24) for v in vertices}

        arbol_bst = Graph(
            vertices, aristas, layout=posiciones, labels=etiquetas,
            vertex_config={"radius": 0.4, "color": BLUE_E, "fill_opacity": 1},
            edge_config={"color": WHITE, "stroke_width": 2}
        )

        self.play(Create(arbol_bst), run_time=3)

        texto_prop = Text("Regla: Subárbol Izquierdo < Raíz < Subárbol Derecho", font_size=24, color=YELLOW).to_edge(
            DOWN)
        self.play(Write(texto_prop, run_time=1.5))
        self.wait(1)

        # SOLUCIÓN: Usamos rectángulos envolventes en lugar de cambiar colores
        cursor_raiz = Circle(radius=0.5, color=YELLOW, stroke_width=4).move_to(posiciones[50])
        self.play(Create(cursor_raiz), run_time=1)

        grupo_nodos_izq = VGroup(arbol_bst.vertices[30], arbol_bst.vertices[20], arbol_bst.vertices[40])
        box_izq = SurroundingRectangle(grupo_nodos_izq, color=GREEN_D, buff=0.2)
        self.play(Create(box_izq), run_time=1.5)
        t_izq = Text("Menores (< 50)", font_size=20, color=GREEN_D).next_to(box_izq, LEFT, buff=0.3)
        self.play(FadeIn(t_izq, shift=RIGHT))
        self.wait(1.5)

        box_der = SurroundingRectangle(arbol_bst.vertices[70], color=RED_D, buff=0.2)
        self.play(Create(box_der), run_time=1.5)
        t_der = Text("Mayores (> 50)", font_size=20, color=RED_D).next_to(box_der, RIGHT, buff=0.3)
        self.play(FadeIn(t_der, shift=LEFT))
        self.wait(5.5)

        self.play(
            FadeOut(box_izq), FadeOut(box_der), FadeOut(cursor_raiz),
            FadeOut(t_izq), FadeOut(t_der), FadeOut(texto_prop), FadeOut(titulo_prop)
        )

        # --- SECCIÓN 3: INSERCIÓN (INSERT) ---
        self.add_sound("audio/03_insercion.mp3")
        titulo_insert = Text("Operación: Insert (key = 25)", font_size=36).to_edge(UP)
        self.play(Write(titulo_insert, run_time=1.5))

        nodo_25 = Circle(radius=0.4, color=GREEN_E, fill_opacity=1).shift(UP * 1.5)
        texto_25 = Text("25", font_size=24).move_to(nodo_25.get_center())
        grupo_25 = VGroup(nodo_25, texto_25)

        self.play(FadeIn(grupo_25, run_time=1.5))
        self.wait(1)

        cursor = Circle(radius=0.5, color=RED, stroke_width=4).move_to(posiciones[50])
        self.play(Create(cursor, run_time=1))

        texto_paso1 = Text("1. 25 < 50 -> Ir a la izquierda (30)", font_size=24).to_edge(DOWN)
        self.play(Write(texto_paso1, run_time=1.5))
        self.wait(1.5)
        self.play(grupo_25.animate.move_to(posiciones[30] + UP * 1.2), cursor.animate.move_to(posiciones[30]),
                  run_time=2)
        self.play(FadeOut(texto_paso1, run_time=1))

        texto_paso2 = Text("2. 25 < 30 -> Ir a la izquierda (20)", font_size=24).to_edge(DOWN)
        self.play(Write(texto_paso2, run_time=1.5))
        self.wait(1.5)
        self.play(grupo_25.animate.move_to(posiciones[20] + UP * 1.2), cursor.animate.move_to(posiciones[20]),
                  run_time=2)
        self.play(FadeOut(texto_paso2, run_time=1))

        texto_paso3 = Text("3. 25 > 20 -> Ir a la derecha (0)", font_size=24).to_edge(DOWN)
        self.play(Write(texto_paso3, run_time=1.5))
        self.wait(1.5)

        pos_final_25 = np.array([-2.5, -3.0, 0])
        self.play(grupo_25.animate.move_to(pos_final_25), FadeOut(cursor, run_time=1), run_time=2)
        self.play(FadeOut(texto_paso3, run_time=1))

        texto_paso4 = Text("4. Crear un nuevo nodo hoja", font_size=24, color=GREEN).to_edge(DOWN)
        self.play(Write(texto_paso4, run_time=1.5))
        linea_20_25 = Line(arbol_bst.vertices[20].get_center(), grupo_25.get_center(), color=WHITE,
                           stroke_width=2).set_z_index(-1)
        self.play(Create(linea_20_25, run_time=1.5))
        self.wait(2.5)
        self.play(FadeOut(texto_paso4), FadeOut(titulo_insert))

        # --- SECCIÓN 4: BÚSQUEDA (SEARCH) ---
        self.add_sound("audio/04_busqueda.mp3")
        titulo_search = Text("Operación: Search (key = 40)", font_size=36).to_edge(UP)
        self.play(Write(titulo_search, run_time=1.5))

        cursor_search = Circle(radius=0.5, color=YELLOW, stroke_width=4).move_to(posiciones[50])
        self.play(Create(cursor_search, run_time=1.5))

        t_search1 = Text("1. 40 < 50 -> Buscar en subárbol izquierdo", font_size=24).to_edge(DOWN)
        self.play(Write(t_search1, run_time=1.5))
        self.wait(1.5)
        self.play(cursor_search.animate.move_to(posiciones[30]), run_time=2)
        self.play(FadeOut(t_search1, run_time=1))

        t_search2 = Text("2. 40 > 30 -> Buscar en subárbol derecho", font_size=24).to_edge(DOWN)
        self.play(Write(t_search2, run_time=1.5))
        self.wait(1.5)
        self.play(cursor_search.animate.move_to(posiciones[40]), run_time=2)
        self.play(FadeOut(t_search2, run_time=1))

        t_search3 = Text("3. 40 == 40 -> ¡Nodo encontrado!", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(t_search3, run_time=1.5))
        self.play(Indicate(cursor_search, color=WHITE, scale_factor=1.2), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(cursor_search), FadeOut(t_search3), FadeOut(titulo_search))

        # --- SECCIÓN 5: ELIMINACIÓN (REMOVE) ---
        self.add_sound("audio/05_eliminacion.mp3")
        titulo_remove = Text("Operación: Remove (key = 40)", font_size=36).to_edge(UP)
        self.play(Write(titulo_remove, run_time=1.5))

        t_remove1 = Text("Caso 1: Nodo Hoja (0 hijos)", font_size=24, color=RED).to_edge(DOWN)
        self.play(Write(t_remove1, run_time=1.5))

        cursor_remove = Circle(radius=0.5, color=RED, stroke_width=4).move_to(posiciones[40])
        self.play(Create(cursor_remove), run_time=1)
        self.wait(2)

        t_remove2 = Text("Se libera la memoria y el puntero del padre cambia a nulo", font_size=24).to_edge(DOWN)
        self.play(ReplacementTransform(t_remove1, t_remove2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(arbol_bst.vertices[40], shift=DOWN), FadeOut(arbol_bst.edges[(30, 40)]),
                  FadeOut(cursor_remove), run_time=2)
        self.wait(3.5)
        self.play(FadeOut(t_remove2), FadeOut(titulo_remove))

        # --- SECCIÓN 6: RECORRIDOS (DFS TRAVERSALS) ---
        self.add_sound("audio/06_recorridos_intro.mp3")
        titulo_trav = Text("Recorridos de Árbol (DFS)", font_size=36).to_edge(UP)
        self.play(Write(titulo_trav, run_time=1.5))

        t_trav_desc = Text("Visitan todos los nodos en un orden sistemático", font_size=24).to_edge(DOWN)
        self.play(Write(t_trav_desc, run_time=1.5))
        self.wait(6.5)
        self.play(FadeOut(t_trav_desc))

        nodos_obj = {
            50: arbol_bst.vertices[50],
            30: arbol_bst.vertices[30],
            70: arbol_bst.vertices[70],
            20: arbol_bst.vertices[20],
            25: grupo_25
        }

        recorridos = [
            ("In-order (Left - Root - Right)", "¡Produce los elementos en orden estrictamente ascendente!",
             [20, 25, 30, 50, 70], YELLOW),
            ("Pre-order (Root - Left - Right)", "Útil para clonar o serializar la estructura del árbol",
             [50, 30, 20, 25, 70], ORANGE),
            ("Post-order (Left - Right - Root)", "Se usa para liberar memoria y evaluar expresiones",
             [25, 20, 30, 70, 50], PURPLE)
        ]

        # SOLUCIÓN: Usamos un cursor móvil en lugar de alterar los colores
        cursor_trav = Circle(radius=0.5, color=WHITE, stroke_width=4)

        audios_recorridos = [
            "audio/07_inorder.mp3",
            "audio/08_preorder.mp3",
            "audio/09_postorder.mp3"
        ]

        for (nombre, desc, seq, color), audio in zip(recorridos, audios_recorridos):
            self.add_sound(audio)
            t_nombre = Text(nombre, font_size=28, color=color).to_edge(DOWN).shift(UP * 0.8)
            t_desc = Text(desc, font_size=20).next_to(t_nombre, DOWN)
            self.play(Write(t_nombre), Write(t_desc), run_time=1.5)

            seq_text = VGroup(*[Text(str(val), font_size=32, color=color) for val in seq])
            seq_text.arrange(RIGHT, buff=0.6).next_to(titulo_trav, DOWN, buff=0.8)

            cursor_trav.set_color(color)

            for i, val in enumerate(seq):
                if i == 0:
                    cursor_trav.move_to(nodos_obj[val].get_center())
                    self.play(FadeIn(cursor_trav), run_time=0.4)
                else:
                    self.play(cursor_trav.animate.move_to(nodos_obj[val].get_center()), run_time=0.6)

                self.play(FadeIn(seq_text[i], shift=UP), run_time=0.4)

            self.wait(4.5)
            self.play(FadeOut(t_nombre), FadeOut(t_desc), FadeOut(seq_text), FadeOut(cursor_trav))

        self.wait(2)
