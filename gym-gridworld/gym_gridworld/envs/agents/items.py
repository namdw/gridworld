import numpy as np 

class Item:
    def __init__(self, env, pos=[0,0], idx=0, value=1, size=3):
        self.map = env
        self.size = size
        self.pos = np.clip(pos, self.map.min, self.map.max-self.size)
        self.id = idx
        self.value = value
        self.status = True

    def hide(self):
        self.status = False

