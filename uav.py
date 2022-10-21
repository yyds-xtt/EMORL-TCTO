import numpy as np

class UAV(object):

    def __init__(self, start_pos):
        self.pos = start_pos

    def move(self, direction_angle: float, distance: float):
        self.pos += distance * np.array([np.cos(direction_angle), np.sin(direction_angle)])

