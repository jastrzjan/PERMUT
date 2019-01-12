from psychopy import visual
from os.path import join


class Permutation:
    def __init__(self, win, elements, pos, size, offset):
        self.fig = elements
        self._elements = []
        for n, name in enumerate(elements):
            pos_x = pos[0] - (len(elements) / 2 - n) * (size + offset)
            pos_y = pos[1]
            item = visual.ImageStim(win=win, image=join('images', 'figures', name), interpolate=True,
                                    size=size, pos=(pos_x, pos_y))
            self._elements.append(item)

    def setAutoDraw(self, draw):
        for stim in self._elements:
            stim.setAutoDraw(draw)

    def check_permutation(self, task):
        for elem1, elem2 in zip(self.fig[:-1], self.fig[1:]):
            for t1, t2 in zip(task.fig[:-1], task.fig[1:]):
                if (elem1 == t1 and elem2 == t2) or (elem1 == t2 and elem2 == t1):
                    return "wrong"
        return "answer"
