import torch
import torch.nn as nn
from torch.functional import F


class TargetNetwork(nn.Module):
    def __init__(self, state_dim, action_dim, hidden_dim=64):
        super().__init__()
        self.fc1 = nn.Linear(state_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, action_dim)

    def forward(self, x):
        t1 = F.tanh(self.fc1(x))
        t2 = F.tanh(self.fc2(t1))
        return F.sigmoid(self.fc3(t2))
