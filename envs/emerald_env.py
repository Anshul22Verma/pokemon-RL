import gymnasium as gym
from gymnasium import spaces

from mgba.core import load_path

import numpy as np

ACTIONS = [
    None,
    "A",
    "B",
    "LEFT",
    "RIGHT",
    "UP",
    "DOWN",
    "START"
]


class PokemonEmeraldEnv(gym.Env):

    def __init__(self, rom_path):

        super().__init__()

        self.core = load_path(rom_path)

        self.action_space = spaces.Discrete(len(ACTIONS))

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(240, 160, 3),
            dtype=np.uint8
        )

        self.steps = 0

        self.seen_frames = set()

    def _get_frame(self):

        video = self.core.video

        frame = np.frombuffer(
            video.buffer,
            dtype=np.uint8
        ).reshape((240, 160, 4))

        frame = frame[:, :, :3]

        return frame

    def _release_all(self):

        try:
            self.core.set_keys(0)
        except:
            pass

    def _press_button(self, action):

        self._release_all()

        if action == "A":
            self.core.set_keys(1)

        elif action == "B":
            self.core.set_keys(2)

        elif action == "SELECT":
            self.core.set_keys(4)

        elif action == "START":
            self.core.set_keys(8)

        elif action == "RIGHT":
            self.core.set_keys(16)

        elif action == "LEFT":
            self.core.set_keys(32)

        elif action == "UP":
            self.core.set_keys(64)

        elif action == "DOWN":
            self.core.set_keys(128)

    def reset(self, seed=None, options=None):

        self.core.reset()

        self.steps = 0

        for _ in range(300):
            self.core.run_frame()

        obs = self._get_frame()

        return obs, {}

    def step(self, action):

        self.steps += 1

        action_name = ACTIONS[action]

        if action_name is not None:
            self._press_button(action_name)

        for _ in range(4):
            self.core.run_frame()

        obs = self._get_frame()

        reward = 0.01

        frame_hash = obs.tobytes()

        if frame_hash not in self.seen_frames:
            reward += 1
            self.seen_frames.add(frame_hash)

        terminated = False

        truncated = self.steps > 10000

        info = {}

        return obs, reward, terminated, truncated, info

    def render(self):
        pass

    def close(self):
        pass