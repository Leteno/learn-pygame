from datetime import datetime

class ElapsingTool:
    def __init__(self, interval, after=0, calculor=lambda x: x):
        self.time = interval
        self.after = after
        self.startTime = None
        self.calcular = calculor
        self.kicked = False

    def isDone(self):
        if not self.startTime:
            return False
        return (datetime.now() - self.startTime).total_seconds() * 1000 > self.time + self.after

    def kick(self):
        if not self.kicked:
            self.startTime = datetime.now()
            self.kicked = True

    def reverse(self):
        def newPercentage(self):
            return 1 - self.percentage()
        self.percentage = newPercentage

    def percentage(self):
        if not self.startTime:
            return 0
        gap = int((datetime.now() - self.startTime).total_seconds() * 1000)
        gap -= self.after
        if gap > self.time:
            gap = self.time
        if gap < 0:
            gap = 0

        return self.calcular(gap / self.time)

