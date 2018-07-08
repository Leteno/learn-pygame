
from runnable.sequence import ElapsingTool

class Task:
    def __init__(self):
        self.seqs = {}
        self.before = []
        self._beforeDelay = None
        self.after = []
        self._afterDelay = None

        self.onBeforeFinishCallback = None
        self.onMainFinishCallback = None
        self.onAfterFinishCallback = None


    def put(self, name, sequence):
        functions = ['process', 'getElapsingTool']
        for f in functions:
            assert hasattr(sequence, f), "sequence: %s has not function '%s'" % (sequence, f)
        self.seqs[name] = sequence

    def remove(self, name):
        if name in self.seqs:
            del self.seqs[name]

    def process(self):
        # before
        beforeNotFinish = False
        for b in self.before:
            b.process()
            if not b.isDone():
                beforeNotFinish = True
        if beforeNotFinish:
            return
        if self._beforeDelay and not self._beforeDelay.isDone():
            return
        self.onBeforeFinish()

        # current
        for x in self.seqs:
            seq = self.seqs[x]
            seq.process()
        if not self.isDone():
            return
        self.onMainFinish()

        # after
        afterNotFinish = False
        if self._afterDelay and not self._afterDelay.isDone():
            return
        for a in self.after:
            a.process()
            if not a.isDone():
                afterNotFinish = True
        if afterNotFinish:
            return
        self.onAfterFinish()

    def onBeforeFinish(self):
        if self.onBeforeFinishCallback:
            self.onBeforeFinishCallback()

    def onMainFinish(self):
        if self.onMainFinishCallback:
            self.onMainFinishCallback()

    def onAfterFinish(self):
        if self.onAfterFinishCallback:
            self.onAfterFinishCallback()

    def addAfter(self, task):
        assert isinstance(task, Task), '%s should be instance of Task' % task
        self.after.append(task)

    def afterDelay(self, delay):
        self._afterDelay = ElapsingTool(delay)

    def addBefore(self, task):
        assert isinstance(task, Task), '%s should be instance of Task' % task
        self.before.append(task)

    def beforeDelay(self, delay):
        self._beforeDelay = ElapsingTool(delay)
    
    def isDone(self):
        for x in self.seqs:
            seq = self.seqs[x]
            elapsingTool = seq.getElapsingTool()
            if not elapsingTool.isDone():
                return False
        return True
