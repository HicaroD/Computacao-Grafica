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
        glutDisplayFunc(self.display)
        glClearColor(1, 1, 1, 1)

    def _draw_green_background(self):
        glColor3f(0, 0.5, 0)
        glVertex2f(-0.5, -0.5)
        glVertex2f(-0.5, 0.5)
        glVertex2f(0.5, 0.5)
        glVertex2f(0.5, -0.5)

    def _draw_yellow_diamond(self):
        glColor3f(1, 1, 0)
        glVertex2f(-0.5, 0)
        glVertex2f(0, 0.5)
        glVertex2f(0.5, 0)
        glVertex2f(0, -0.5)

    def draw_flag(self):
        glBegin(GL_QUADS)
        self._draw_green_background()
        self._draw_yellow_diamond()
        glEnd()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        gluOrtho2D(-1, 1, -1, 1)
        self.draw_flag()
        glFlush()

    def run(self) -> None:
        glutMainLoop()


def main():
    drawer = Drawer()
    drawer.run()


if __name__ == "__main__":
    main()
