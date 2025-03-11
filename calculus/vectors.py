from manim import *

class Vector3DScene(ThreeDScene):
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