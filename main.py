import random

import torch.cuda
from torch.optim import Adam

from config import RLConfig, EnvConfig
from network import TargetNetwork
from uav import UAV
from smart_device import SD
from environment import Env
from utils import *

def TPU(P, _P, Z_ref, P_num: int, P_size: int):
    # generate P_num evenly distributed weight vectors
    W = weight_200[:P_num]
    # set performance buffer
    B = [[] for i in range(P_num)]
    # for every learning task

        # calculate objective vector

        # set F_temp

        # set index

        # store task in buffer[index]

        # calculate distance between F(\pi_\theta) and Z_ref

        # if |buffer[index]| > P_size

            # sort all tasks in buffer[index] in descending order of their distances

            # retain first P_size tasks in buffer[index]

    # set new task population P_new
    return sum(B, start=[])


def collect_trajectories(pi_old):
    env = Env()
    trajectories = []
    for t in range(EnvConfig.T):
        pass

    pass


def MMPPO(Omega, n_iter):
    _P = []

    for (w, pi, pi_old, v) in Omega:
        for j in range(n_iter):
            # collect trajectories set

            # calculate A_t

            # calculate A_t^{w_t}

            # update target and sample policy networks and value network

            # store the updated new task

            j += 1
            pass

    return _P


# warm-up stage
device = 'cuda' if torch.cuda.is_available() else 'cpu'


P = []
EP = []
weight_vectors = generate_weight_vector_explicitly_evenly(RLConfig.n)

# initialize policy networks
target_policy_networks = [TargetNetwork(4, 3).to(device) for _ in range(RLConfig.n)]
sample_policy_networks = [target_policy_networks[i].copy() for i in range(RLConfig.n)]

# initialize value networks
value_networks = [TargetNetwork(3, 3).to(device) for _ in range(RLConfig.n)]

# denote the task set
task_set = [(weight_vectors[i], target_policy_networks[i], sample_policy_networks[i], value_networks[i])
            for i in range(RLConfig.n)]

# obtain offspring population
P_ = MMPPO(task_set, RLConfig.n_warm)

for l in range(RLConfig.G_max):
    # update task population

    # update EP

    task_set = []

    # calculate F(\pi_{\theta_j})

    for w_i in weight_vectors:
        # set index

        # replace weight vector

        # add task
        pass
    pass

    # obtain offspring population
    P_ = MMPPO(task_set, RLConfig.n_evo)