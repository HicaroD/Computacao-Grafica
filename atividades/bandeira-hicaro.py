from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Drawer:
    def __init__(self) -> None:
        glutInit()
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        glutCreateWindow("Brazilian Flag")

    def _draw_green_background(self):
        glColor3f(0, 0.5, 0)
        vertexes = [
            (-0.5, -0.5),
            (-0.5, 0.5),
            (0.5, 0.5),
            (0.5, -0.5),
        ]
        for vertex in vertexes:
            glVertex2f(vertex[0], vertex[1])

    def _draw_yellow_diamond(self):
        glColor3f(1, 1, 0)

        vertexes = [
            (-0.5, 0),
            (0, 0.5),
            (0.5, 0),
            (0, -0.5),
        ]
        for vertex in vertexes:
            glVertex2f(vertex[0], vertex[1])

    def draw_flag(self):
        glBegin(GL_QUADS)
        self._draw_green_background()
        self._draw_yellow_diamond()
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        gluOrtho2D(-10, 10, -10, 10)
        self.draw_flag()
        glFlush()

    def run(self) -> None:
        glutDisplayFunc(self.display)
        glClearColor(1, 1, 1, 1)
        glutMainLoop()


def main():
    drawer = Drawer()
    drawer.run()


if __name__ == "__main__":
    main()
