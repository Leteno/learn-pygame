
from widget.view.Drawwer import Drawwer

class ImageView(Drawwer):
    def __init__(self, surf):
        self.surf = surf

    def onDraw(self, canvas, position):
        rect = self.surf.get_rect()
        rect.center = position
        canvas.blit(self.surf, rect)
