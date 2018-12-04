import numpy as np
from gym_gridworld.envs.agents.movers import Mover

class Player(Mover):
    def __init__(self, env, pos=[0,0], mode='normal', size=1):
       super(Player, self).__init__(env, pos=pos, size=size)
       self.score = 0
    
    def setScore(self, score):
        self.score = score
