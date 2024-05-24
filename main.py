import pyxel


class Main:
    def __init__(self):
        pyxel.init(128, 128, title="NDC")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)


if __name__ == '__main__':
    main = Main()
