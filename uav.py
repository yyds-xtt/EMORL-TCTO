from typing import List

import numpy as np
from config import EnvConfig


class UAV(object):

    def __init__(self, start_pos: List,
                 P1: float,
                 P2: float,
                 U_tip: float,
                 d0: float,
                 rho: float,
                 g: float,
                 A: float):
        self.pos = np.array(start_pos)
        self.P1 = P1
        self.P2 = P2
        self.U_tip = U_tip
        self.d0 = d0
        self.rho = rho
        self.g = g
        self.A = A

    def move(self, direction_angle: float, distance: float):
        self.pos += distance * np.array([np.cos(direction_angle), np.sin(direction_angle)])

    
