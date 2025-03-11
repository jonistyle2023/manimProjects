from manim import *
import numpy as np

## Primera salida
class vector3DScene(ThreeDScene):
    def construct(self):
        # Configuración de los ejes 3D
        axes = ThreeDAxes()

        # Definir el vector v = (3, -8, 10)
        vector = Arrow3D(start=ORIGIN, end=[3, -8, 10], color=RED)

        # Etiqueta del vector
        label = MathTex(r"\mathbf{v} = (3, -8, 10)").next_to(vector.get_end(), RIGHT, buff=0.5)

        # Configuración de la cámara
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Animaciones
        self.add(axes, vector, label)
        self.wait(3)

## Vector unitario de la tarea
class vector3DAnimation(ThreeDScene):
    def construct(self):
        # Configurar ejes 3D
        ejes = ThreeDAxes()
        self.add(ejes)

        # Coordenadas de los puntos
        A = [-1, 5, -4]
        B = [2, -3, 6]
        vector = [3, -8, 10]  # Componentes calculadas

        # Crear esferas para los puntos
        punto_A = Dot3D(point=A, color=RED, radius=0.1)
        punto_B = Dot3D(point=B, color=BLUE, radius=0.1)

        # Etiquetas de texto fijas en la pantalla
        etiqueta_A = Tex("A(-1, 5, -4)", color=RED).to_corner(UL)
        etiqueta_B = Tex("B(2, -3, 6)", color=BLUE).next_to(etiqueta_A, DOWN)
        componentes = MathTex(r"\mathbf{v} = (3, -8, 10)", color=GREEN).next_to(etiqueta_B, DOWN)
        unitario = MathTex(r"\mathbf{u} = \left(\frac{3}{\sqrt{173}},\frac{-8}{\sqrt{173}},\frac{10}{\sqrt{173}}\right)", color=YELLOW).next_to(componentes, DOWN)

        # Flecha 3D personalizada
        flecha = Arrow3D(
            start=A,
            end=B,
            color=GREEN,
            thickness=0.02  # Ajusta el grosor de la flecha
        )

        # Añadir elementos fijos en la pantalla
        self.add_fixed_in_frame_mobjects(etiqueta_A, etiqueta_B, componentes, unitario)

        # Añadir objetos 3D al escenario
        self.add(ejes, punto_A, punto_B, flecha)

        # Configurar cámara y animación
        self.set_camera_orientation(phi=75*DEGREES, theta=30*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)  # Rotación continua
        self.wait(12)  # Duración para una rotación completa
        self.stop_ambient_camera_rotation()