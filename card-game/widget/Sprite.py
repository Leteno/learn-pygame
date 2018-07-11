
from widget.view.Drawwer import Drawwer

class Sprite:
    def __init__(self, drawwer, position=(0, 0)):
        assert isinstance(drawwer, Drawwer), 'drawwer %s should be instance of Drawwer' % drawwer
        self.drawwer = drawwer
        self.position = position

    def draw(self, canvas):
        self.drawwer.draw(canvas, self.position)

    def show(self):
        self.drawwer.show()

    def hide(self):
        self.drawwer.hide()
