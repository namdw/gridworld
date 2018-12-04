import numpy as np

class Mover:
    def __init__(self, env, mode='normal', pos=None, size=None):
        self.map = env
        self.size = size
        self.pos = np.clip(pos, self.map.min, self.map.max-self.size)
        self.mode = mode
        self.a_dict = {0:(1,0), 1:(0,1), 2:(-1,0), 3:(0,-1)}
        self.a_space = 4
        self.prev_a = None
        self.curr_a = None
        if mode=='extra':
            ea_dict = {4:(1,1), 5:(1,-1), 6:(-1,-1), 7:(-1,1)}
            self.a_dict = self.a_dcit.update(ea_dict)
            self.a_space = 8

    def move(self, a):
        assert a<self.a_space
        self.prev_a = self.curr_a
        self.curr_a = a
        self.pos += self.a_dict[a]
        self.pos = np.clip(self.pos, self.map.min, self.map.max-self.size-1)
        return self.pos

