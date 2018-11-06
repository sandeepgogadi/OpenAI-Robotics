import gym
import gym.spaces

env = gym.make('FetchPush-v1')

for i in range(5):
    observation = env.reset()
    for j in range(10):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if i == 0 and j == 0:
            print('action observation reward done info')
            print(type(action), type(observation), type(reward), type(done), type(info))

        print(action, observation, reward, done, info)

        if done:
            break
