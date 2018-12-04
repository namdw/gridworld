import numpy as np
from gym_gridworld.envs.agents.movers import Mover

class Npc(Mover):
    def __init__(self, env, pos=[0,0], mode='normal', size=1):
        super(Npc, self).__init__(env, pos=pos, mode=mode, size=size)

