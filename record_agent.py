import cv2

from stable_baselines3 import PPO

from envs.emerald_env import PokemonEmeraldEnv


env = PokemonEmeraldEnv(
    "roms/Pokemon_Emerald.gba"
)

model = PPO.load(
    "checkpoints/emerald_speedrunner"
)

obs, _ = env.reset()

writer = cv2.VideoWriter(
    "recordings/emerald_run.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    30,
    (160, 240)
)

while True:

    action, _ = model.predict(obs)

    obs, reward, terminated, truncated, info = env.step(action)

    frame = obs[:, :, ::-1]

    frame = cv2.resize(
        frame,
        (160, 240)
    )

    writer.write(frame)

    cv2.imshow("Emerald RL", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if terminated or truncated:
        break

writer.release()

cv2.destroyAllWindows()