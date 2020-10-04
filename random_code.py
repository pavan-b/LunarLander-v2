import numpy as np
import gym

# make the environment of a game
# env = gym.make('LunarLander-v2')
env = gym.make('AirRaid-v0')
# env.render()

# the action space
print(env.action_space)

# the state space
print(env.observation_space)


# one sample step
observation = env.reset()
print(observation.shape)

# take an action in the environment
# action = env.action_space.sample()
# observation, reward, done, info = env.step(action)
# print(observation)
# print(reward)
# print(done)
# print(info)
# print(action)



# run for a few episodes
# at the start of each episode, reset the environment 
#
env.close()