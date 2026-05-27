from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv

from env import EmeraldEnv


def make_env():
    return EmeraldEnv()


if __name__ == "__main__":

    env = DummyVecEnv([make_env])

    model = PPO(
        "CnnPolicy",
        env,
        verbose=1,
        n_steps=1024,
        batch_size=64,
        learning_rate=3e-4,
        gamma=0.99
    )

    model.learn(total_timesteps=200_000)

    model.save("checkpoints/emerald_ppo")