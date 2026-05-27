from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

from envs.emerald_env import PokemonEmeraldEnv


def make_env():

    return PokemonEmeraldEnv(
        "roms/Pokemon_Emerald.gba"
    )


env = DummyVecEnv([make_env])

model = PPO(
    "CnnPolicy",
    env,
    verbose=1,
    tensorboard_log="./logs/",
    learning_rate=0.0003,
    batch_size=64,
    n_steps=2048,
)

model.learn(
    total_timesteps=1_000_000
)

model.save(
    "checkpoints/emerald_speedrunner"
)