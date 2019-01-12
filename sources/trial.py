import numpy as np
from os import listdir
from os.path import join
from sources.permutation import Permutation


class Trial:
    def __init__(self, win, config, n_elements=4):
        self.n_elements = n_elements
        fig = np.random.choice([f for f in listdir(join("images", "figures"))], n_elements, replace=False)
        self.task = Permutation(win=win, elements=fig, pos=config["TASK_POS"],
                                size=config["FIG_SIZE"], offset=config["FIG_OFFSET"])

        self.answers = []
        ans_pos = np.random.choice(range(3))
        for i in range(3):
            while True:
                perm = np.random.permutation(fig)
                ans = Permutation(win=win, elements=perm,
                                  pos=config["ANSWERS_{}_POS".format(i+1)],
                                  size=config["FIG_SIZE"], offset=config["FIG_OFFSET"])

                if (ans.check_permutation(self.task) == "answer" and i == ans_pos) or \
                   (ans.check_permutation(self.task) == "wrong" and i != ans_pos):
                    if len([1 for elem in [f.fig for f in self.answers] if sum(elem==ans.fig)==n_elements]) == 0:
                        print(ans.check_permutation(self.task))
                        print(ans.fig)
                        print(self.task.fig)
                        break
            self.answers.append(ans)

    def set_auto_draw(self, draw=True):
        self.task.setAutoDraw(draw)
        for ans in self.answers:
            ans.setAutoDraw(draw)

    def get_info(self):
        info = {
            'n_elements': self.n_elements,
            'task': self.task,
            'answers': [answer.fig for answer in self.answers]}
        return info
