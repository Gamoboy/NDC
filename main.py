import pyxel
from math import *
import time


class Button:
    def __init__(self, x, y, size_x, size_y):
        self.x = x
        self.y = y
        self.size = [size_x, size_y]

    def update(self):
        pass

    def draw(self, scene_state):
        if scene_state == "Menu":
            pyxel.rect(self.x, self.y, self.size[0], self.size[1], 8)


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = 16
        self.speed = 1
        self.anim_step = 0
        self.anim_lenght = 4
        self.direction = 0

    def update(self):
        pressed = False

        if pyxel.btn(pyxel.KEY_Z) and pyxel.btn(pyxel.KEY_D) and not pressed:
            pressed = True
            self.direction = 1
            self.y -= round(self.speed * (1 / sqrt(2)), 1)
            self.x += round(self.speed * (1 / sqrt(2)), 1)

        if pyxel.btn(pyxel.KEY_Z) and pyxel.btn(pyxel.KEY_Q) and not pressed:
            pressed = True
            self.direction = 1
            self.y -= round(self.speed * (1 / sqrt(2)), 1)
            self.x -= round(self.speed * (1 / sqrt(2)), 1)

        if pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_Q) and not pressed:
            pressed = True
            self.direction = 0
            self.y += round(self.speed * (1 / sqrt(2)), 1)
            self.x -= round(self.speed * (1 / sqrt(2)), 1)

        if pyxel.btn(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_D) and not pressed:
            pressed = True
            self.direction = 0
            self.y += round(self.speed * (1 / sqrt(2)), 1)
            self.x += round(self.speed * (1 / sqrt(2)), 1)

        if pyxel.btn(pyxel.KEY_Z) and not pressed:
            pressed = True
            self.direction = 1
            self.y -= self.speed

        if pyxel.btn(pyxel.KEY_Q) and not pressed:
            pressed = True
            self.direction = 3
            self.x -= self.speed

        if pyxel.btn(pyxel.KEY_S) and not pressed:
            pressed = True
            self.direction = 0
            self.y += self.speed

        if pyxel.btn(pyxel.KEY_D) and not pressed:
            pressed = True
            self.direction = 2
            self.x += self.speed

    def draw(self, scene_state):
        if scene_state == "Game":
            if pyxel.btn(pyxel.KEY_Z) or pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_D) or pyxel.btn(pyxel.KEY_Q):
                    if self.anim_step == (self.anim_lenght * 5)-1:
                        self.anim_step = -1
                    self.anim_step += 1
                    pyxel.blt(self.x, self.y, 0, (self.anim_step // 5) * 16, 8 + self.direction * 16, 16, 16, colkey=5)
                    # pyxel.rect(self.x, self.y, self.size, self.size, 1)
            else:
                self.direction = 1
                pyxel.blt(self.x, self.y, 0, 0, 8, 16, 16, colkey=5)


class Main:
    def __init__(self):
        pyxel.init(256, 256, title="NDC")

        self.fullscreen = False
        self.fullscreen_toogle = False
        self.show_cursor = False

        self.scene_state = "Game"

        self.objects = []
        self.objects.append(Player())

        self.objects.append(Button(30, 30, 200, 50))
        self.objects.append(Button(90, 110, 70, 20))
        self.objects.append(Button(90, 140, 70, 20))
        self.objects.append(Button(90, 170, 70, 20))

        pyxel.load("theme2.pyxres")

        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.show_cursor and self.scene_state == "Menu":
            self.show_cursor = True
            pyxel.mouse(True)
        elif self.show_cursor and not self.scene_state == "Menu":
            self.show_cursor = False
            pyxel.mouse(True)
        if pyxel.btn(pyxel.KEY_F):
            if not self.fullscreen_toogle:
                self.fullscreen_toogle = True
                if self.fullscreen:
                    self.fullscreen = False
                    pyxel.fullscreen(False)
                else:
                    self.fullscreen = True
                    pyxel.fullscreen(True)
        else:
            self.fullscreen_toogle = False

        for object in self.objects:
            object.update()

    def draw(self):
        pyxel.cls(0)

        for object in self.objects:
            object.draw(self.scene_state)


if __name__ == '__main__':
    main = Main()