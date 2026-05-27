import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import os
import time


ACTIONS = ["NONE", "A", "B", "UP", "DOWN", "LEFT", "RIGHT"]


class EmeraldEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(len(ACTIONS))

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(144, 160, 3),
            dtype=np.uint8
        )

        self.input_file = "input.txt"
        self.frame_file = "frame.png"

        self.last_obs = np.zeros((144, 160, 3), dtype=np.uint8)

    def _write_action(self, action):
        with open(self.input_file, "w") as f:
            f.write(ACTIONS[action])

    def _read_frame(self):

        # wait until BizHawk writes frame
        timeout = 2.0
        start = time.time()

        while not os.path.exists(self.frame_file):
            if time.time() - start > timeout:
                return self.last_obs
            time.sleep(0.01)

        img = cv2.imread(self.frame_file)

        if img is None:
            return self.last_obs

        img = cv2.resize(img, (160, 144))

        self.last_obs = img
        return img

    def reset(self, seed=None, options=None):
        obs = self._read_frame()
        return obs, {}

    def step(self, action):

        self._write_action(action)

        obs = self._read_frame()

        # minimal reward (placeholder)
        reward = 0.01

        terminated = False
        truncated = False

        info = {}

        return obs, reward, terminated, truncated, info

    def close(self):
        pass