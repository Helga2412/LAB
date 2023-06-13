import gym
from pprint import pprint

def main():
    state, action = 0, 0
    env = gym.make("Acrobot-v1")
    print('Пространство состояний:')
    pprint(env.observation_space)
    print()
    print('Пространство действий:')
    pprint(env.action_space)
    print()
    print('Диапазон наград:')
    pprint(env.reward_range)


if __name__ == '__main__':
    main()