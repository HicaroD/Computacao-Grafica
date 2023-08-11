import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import pygame as pg
from pygame.locals import *

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Drawer:
    def __init__(self) -> None:
        # glutInit()
        # glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        # glutInitWindowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        # glutCreateWindow("Brazilian Flag")
        self.green_background_vertexes = [
            [-0.5, -0.5, 1],
            [-0.5, 0.5, 1],
            [0.5, 0.5, 1],
            [0.5, -0.5, 1],
        ]
        self.yellow_diamond_vertexes = [
            [-0.5, 0, 1],
            [0, 0.5, 1],
            [0.5, 0, 1],
            [0, -0.5, 1],
        ]

    def draw_flag(self):
        glBegin(GL_QUADS)
        self._draw_green_background()
        self._draw_yellow_diamond()
        glEnd()

    def translate(self, x, y):
        translation_matrix = [
            [1, 0, x],
            [0, 1, y],
            [0, 0, 1],
        ]
        self._translate_green_background(translation_matrix)
        self._translate_yellow_diamond(translation_matrix)

    def _translate_green_background(self, translation_matrix):
        translated_matrix = []
        for vertex in self.green_background_vertexes:
            result = numpy.matmul(translation_matrix, vertex)
            print(result)
            translated_matrix.append(result)
        self.green_background_vertexes = translated_matrix

    def _translate_yellow_diamond(self, translation_matrix):
        translated_matrix = []
        for vertex in self.yellow_diamond_vertexes:
            result = numpy.matmul(translation_matrix, vertex)
            translated_matrix.append(result)
        self.yellow_diamond_vertexes = translated_matrix

    def rotate(self, degrees, counterclockwise=False):
        rotation_matrix = [
            [math.cos(degrees), math.sin(degrees), 0],
            [-math.sin(degrees), math.cos(degrees), 0],
            [0, 0, 1],
        ]

        if counterclockwise:
            rotation_matrix[0][1] *= -1
            rotation_matrix[1][0] *= -1

        self._rotate_green_background(rotation_matrix)
        self._rotate_yellow_diamond(rotation_matrix)

    def _rotate_green_background(self, rotation_matrix):
        rotated_matrix = []
        for vertex in self.green_background_vertexes:
            result = numpy.matmul(vertex, rotation_matrix)
            rotated_matrix.append(result)
        self.green_background_vertexes = rotated_matrix

    def _rotate_yellow_diamond(self, rotation_matrix):
        rotated_matrix = []
        for vertex in self.yellow_diamond_vertexes:
            result = numpy.matmul(vertex, rotation_matrix)
            rotated_matrix.append(result)
        self.yellow_diamond_vertexes = rotated_matrix

    def scale(self, x: float, y: float):
        scaling_matrix = [
            [x, 0, 0],
            [0, y, 0],
            [0, 0, 1],
        ]
        self._scale_green_background(scaling_matrix)
        self._scale_yellow_diamond_vertexes(scaling_matrix)

    def _scale_green_background(self, scaling_matrix):
        scaled_matrix = []
        for vertex in self.green_background_vertexes:
            result = numpy.matmul(scaling_matrix, vertex)
            scaled_matrix.append(result)
        self.green_background_vertexes = scaled_matrix

    def _scale_yellow_diamond_vertexes(self, scaling_matrix):
        scaled_matrix = []
        for vertex in self.yellow_diamond_vertexes:
            result = numpy.matmul(scaling_matrix, vertex)
            scaled_matrix.append(result)
        self.yellow_diamond_vertexes = scaled_matrix

    def _draw_green_background(self):
        glColor3f(0, 0.5, 0)
        for vertex in self.green_background_vertexes:
            glVertex2f(vertex[0], vertex[1])

    def _draw_yellow_diamond(self):
        glColor3f(1, 1, 0)
        for vertex in self.yellow_diamond_vertexes:
            glVertex2f(vertex[0], vertex[1])

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        gluOrtho2D(-10, 10, -10, 10)
        self.draw_flag()
        glFlush()

    def handle_key_down(self, key_pressed):
        match key_pressed:
            case pg.K_LEFT:
                self.translate(-1, 0)
            case pg.K_UP:
                self.translate(0, 1)
            case pg.K_DOWN:
                self.translate(0, -1)
            case pg.K_RIGHT:
                self.translate(1, 0)
            case pg.K_SPACE:
                self.rotate(2)
            case pg.K_LCTRL:
                self.scale(1.5, 1.5)
            case pg.K_RCTRL:
                self.scale((1 / 1.5), (1 / 1.5))

    def run(self) -> None:
        pg.init()
        display = (580, 580)
        pg.display.set_mode(display, DOUBLEBUF | OPENGL)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                if event.type == pg.KEYDOWN:
                    self.handle_key_down(event.key)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glClearColor(1, 1, 1, 1)
            self.display()
            pg.display.flip()
            pg.time.wait(10)


def main():
    drawer = Drawer()
    drawer.run()


if __name__ == "__main__":
    main()
