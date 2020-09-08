import copy
import os
import random
from collections import namedtuple, deque

import numpy as np
import torch
import torch.nn.functional as F
import torch.optim as optim

from model import Actor, Critic

GAMMA = 0.99                    # discount factor
TAU = 5e-2                      # for soft update of target parameters
LR_ACTOR = 5e-4                 # learning rate of the actor
LR_CRITIC = 5e-4                # learning rate of the critic
WEIGHT_DECAY = 0.0              # L2 weight decay
NOISE_AMPLIFICATION = 1         # exploration noise amplification
NOISE_AMPLIFICATION_DECAY = 1   # noise amplification decay
