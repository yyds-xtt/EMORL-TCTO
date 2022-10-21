import random

from config import EnvConfig
from smart_device import SD


class Env(object):
    def __init__(self):
        self.device_num = EnvConfig.K
        self.sds = [
            SD(
                zeta=random.choice(EnvConfig.zetas_candidate),
                pos=[random.random() * EnvConfig.x_max, random.random() * EnvConfig.y_max]
            )
            for i in range(self.device_num)
        ]

    def step(self, action):
        pass
