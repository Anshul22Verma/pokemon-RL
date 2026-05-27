from stable_baselines3 import PPO

from env import EmeraldEnv


env = EmeraldEnv()

model = PPO(
    "CnnPolicy",
    env,
    verbose=1
)

model.learn(
    total_timesteps=100000
)

model.save(
    "emerald_agent"
)