import numpy as np

import gym
import gym_gridworld

env = gym.make('gridworld-v0')

state = env.reset()

for i in range(10000):
    state, reward, done, info = env.step(np.random.randint(4))
    env.render()
    if reward > 0:
        print(reward)
print(state)
