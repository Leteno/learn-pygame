
class Vango:
    def __init__(self):
        self.spriteList = []

    def add(self, sprite):
        self.spriteList.append(sprite)

    def remove(self, sprite):
        self.spriteList.remove(sprite)

    def show(self, canvas):
        for x in self.spriteList:
            x.draw(canvas)
