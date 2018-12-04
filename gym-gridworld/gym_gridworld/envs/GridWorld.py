import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np

from gym_gridworld.envs.agents.player import Player
from gym_gridworld.envs.agents.npc import Npc
from gym_gridworld.envs.agents.items import Item
from gym_gridworld.envs.env.env import GridWorld

class GridWorldEnv(gym.Env):
    metadata = {
            'render.modes' : ['human', 'rgb_array'], 
            'video.frames_per_second' : 50
            }

    def __init__(self):
        self.mode = 'normal'
        if self.mode=='normal':
            self.num_action = 4
        self.size = 84
        self.width = self.size 
        self.height = self.size
        self.action_space = spaces.Discrete(self.num_action)
        self.observation_space = spaces.Box(0, 255, [self.width, self.height], dtype=np.float32)

        self.seed()
        
        self.num_npc = 5
        self.num_item = 5

        self.state = self.reset()

        self.viewer = None

        self.steps_beyond_done = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]
    
    def reset(self):
        self.map = GridWorld(self.size)
        player = Player(self.map, pos=np.random.randint(self.size, size=2), mode=self.mode, size=10)
        self.map.addPlayer(player)
        for i in range(self.num_npc):
            npc = Npc(self.map, pos=np.random.randint(self.size, size=2), mode=self.mode, size=8)
            self.map.addNpc(npc)
        for i in range(self.num_item):
            item = Item(self.map, pos=np.random.randint(self.size, size=2), size=4)
            self.map.addItem(item)
        
        self.steps_beyond_done = None

        return self.map.getState()
        

    def step(self, action):
        reward = 0
        items_left = 0
        done = False
        player = self.map.player
        player.move(action)
        for npc in self.map.npcs:
            if npc.prev_a is not None and np.random.rand() < 0.8:
                npc.move(npc.prev_a)
            else:
                npc.move(np.random.randint(self.num_action))
        for item in self.map.items:
            if item.status and item.pos[0] >= player.pos[0]-item.size+1 and item.pos[0] <= player.pos[0]+player.size-1 \
                    and item.pos[1] >= player.pos[1]-item.size+1 and item.pos[1] <= player.pos[1]+player.size-1:
                        item.hide()
                        player.setScore(player.score+item.value)
                        reward += item.value
            else:
                items_left += 1
        done = bool(-(items_left-1))
        self.state = self.map.getState()

        return self.state, reward, done, None

    def render(self, mode='human'):
        screen_width = self.size
        screen_height = self.size

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)
            self.n_trans = []
            self.i_trans = []
            self.i_geos = []
            for item in self.map.items:
                i_size = item.size
                i_geo = rendering.FilledPolygon([(0,0), (i_size,0), (i_size,i_size), (0,i_size)])
                _i_trans = rendering.Transform()
                self.i_trans.append(_i_trans)
                i_geo.add_attr(_i_trans)
                self.viewer.add_geom(i_geo)
                self.i_geos.append(i_geo)
            p_geo = rendering.FilledPolygon([(0,0), (self.map.player.size,0), (self.map.player.size, self.map.player.size), (0, self.map.player.size)])
            self.p_trans = rendering.Transform()
            p_geo.add_attr(self.p_trans)
            self.viewer.add_geom(p_geo)
            for npc in self.map.npcs:
                n_size = npc.size
                n_geo = rendering.FilledPolygon([(0,0), (n_size,0), (n_size,n_size), (0,n_size)])
                _n_trans = rendering.Transform()
                self.n_trans.append(_n_trans)
                n_geo.add_attr(_n_trans)
                self.viewer.add_geom(n_geo)
            
        if self.state is None: return None

        for item, _i_trans, _i_geo in zip(self.map.items, self.i_trans, self.i_geos):
            _i_trans.set_translation(*item.pos)
            if not item.status:
                _i_geo.set_color(1.0, 1.0, 1.0)
        self.p_trans.set_translation(*self.map.player.pos)
        for npc, _n_trans in zip(self.map.npcs, self.n_trans):
            _n_trans.set_translation(*npc.pos)

        return self.viewer.render(return_rgb_array = mode=='rgb_array')

    
    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None


