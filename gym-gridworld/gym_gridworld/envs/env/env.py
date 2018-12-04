import numpy as np

class GridWorld:
    def __init__(self, size=84):
        self.size = size
        self.min = 0
        self.max = size
        self.player = None 
        self.npcs = []
        self.items = []

        self.num_players = 0
        self.num_npcs = 0
        self.num_items = 0

    def addPlayer(self, new_player):
        self.player = new_player 
        self.num_players = 1

    def addNpc(self, new_npc):
        self.npcs.append(new_npc)
        self.num_npcs += 1

    def addItem(self, new_item):
        self.items.append(new_item)
        self.num_items += 1

    def getState(self):
        state = np.zeros((self.size, self.size))
        for item in self.items:
            if item.status:
                state[item.pos[0]:item.pos[0]+item.size, item.pos[1]:item.pos[1]+item.size] = 0.3
        state[self.player.pos[0]:self.player.pos[0]+self.player.size, self.player.pos[1]:self.player.pos[1]+self.player.size] = 1
        for npc in self.npcs:
            state[npc.pos[0]:npc.pos[0]+npc.size, npc.pos[1]:npc.pos[1]+npc.size] = 0.6

        return state

