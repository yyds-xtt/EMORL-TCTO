from typing import List
from scipy import stats


class SD(object):
    def __init__(self, zeta: float,
                 pos: List):
        self.pos = pos
        self.task_generator = stats.bernoulli(zeta)

    def generate_a_task(self) -> bool:
        return self.task_generator.rvs(1)[0] == 1
