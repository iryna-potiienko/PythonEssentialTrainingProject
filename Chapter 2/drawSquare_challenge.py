import os
import time
from termcolor import colored

class Canvas:
    def __init__(self, width, height):
        self._x = width
        self._y = height
        self._canvas = [[' ' for y in range(self._y)] for x in range(self._x)]

    def hitsWall(self, point):
        return point[0] < 0 or point[0] >= self._x or point[1] < 0 or point[1] >= self._y

    def setPos(self, pos, mark):
        self._canvas[pos[0]][pos[1]] = mark

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print(self):
        self.clear()
        for y in range(self._y):
            print(' '.join([col[y] for col in self._canvas]))

class TerminalScribe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.trail = '.'
        self.mark = '*'
        self.framerate = 0.2
        self.pos = [0, 0]

    def up(self):
        pos = [self.pos[0], self.pos[1]-1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def down(self):
        pos = [self.pos[0], self.pos[1]+1]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def right(self):
        pos = [self.pos[0]+1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def left(self):
        pos = [self.pos[0]-1, self.pos[1]]
        if not self.canvas.hitsWall(pos):
            self.draw(pos)

    def draw(self, pos):
        self.canvas.setPos(self.pos, self.trail)
        self.pos = pos
        self.canvas.setPos(self.pos, colored(self.mark, 'red'))
        self.canvas.print()
        time.sleep(self.framerate)


class FigureScriber:
    def __init__(self, x, y):
        self.canvas = Canvas(x, y)
        self.scriber = TerminalScribe(self.canvas)

    def drowSquare(self, length):
        leng = length - 1
        for i in range(leng):
            self.scriber.right()

        for i in range(leng):
            self.scriber.down()

        for i in range(leng):
            self.scriber.left()

        for i in range(leng):
            self.scriber.up()

    def drowRechtangle(self, length, height):
        leng = length - 1
        hei = height - 1
        for i in range(leng):
            self.scriber.right()

        for i in range(hei):
            self.scriber.down()

        for i in range(leng):
            self.scriber.left()

        for i in range(hei):
            self.scriber.up()


figureScribe = FigureScriber(30, 30)
# figureScribe.drowSquare(5)
figureScribe.drowRechtangle(4, 8)



