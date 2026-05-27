import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import time
import os

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

        self.frame_file = "frame.raw"
        self.input_file = "input.txt"

    def _write_action(self, action):
        with open(self.input_file, "w") as f:
            f.write(ACTIONS[action])

    def _get_frame(self):
        while not os.path.exists(self.frame_file):
            time.sleep(0.01)

        data = np.fromfile(self.frame_file, dtype=np.uint8)

        # BizHawk screenshot is raw PNG-like bytes, so decode via OpenCV
        frame = cv2.imdecode(data, cv2.IMREAD_COLOR)

        if frame is None:
            return np.zeros((144, 160, 3), dtype=np.uint8)

        frame = cv2.resize(frame, (160, 144))

        return frame

    def reset(self, seed=None, options=None):
        return self._get_frame(), {}

    def step(self, action):

        self._write_action(action)

        obs = self._get_frame()

        reward = 0.01

        return obs, reward, False, False, {}