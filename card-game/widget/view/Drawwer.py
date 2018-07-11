
class Drawwer:

    shown = True

    def draw(self, canvas, position):
        if self.shown:
            self.onDraw(canvas, position)

    def onDraw(self, canvas, position):
        pass

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False
