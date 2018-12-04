custom gym env for gridworld 

## Install
run pip install -e . inside gym-gridworld to install

## Use
```
import gym
import gym_gridworld
```

then use same as other gym envs with 
```
env = gym.make('gridworld-v0')
```

## TODO
- add wrapper for multiple env using mpi
- add wrapper for allowing hyperparameter settings such as 
	- number of npcs
	- number of items and their rewards
	- size of the map, player, npc, item
	- color of map, player, npc, item
