import gymnasium as gym
from gymnasium import spaces
import numpy as np
import cv2
import os

ACTIONS = ["NONE","A","B","UP","DOWN","LEFT","RIGHT"]

class Env(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(len(ACTIONS))

        self.observation_space = spaces.Box(
            0, 255, shape=(144,160,3), dtype=np.uint8
        )

        self.input_file = "input.txt"
        self.img_file = "frame.png"

    def _write_action(self, a):
        with open(self.input_file, "w") as f:
            f.write(ACTIONS[a])

    def _read_frame(self):
        img = cv2.imread(self.img_file)

        if img is None:
            return np.zeros((144,160,3), dtype=np.uint8)

        return cv2.resize(img, (160,144))

    def reset(self):
        return self._read_frame(), {}

    def step(self, action):

        self._write_action(action)

        obs = self._read_frame()

        reward = 0.01

        return obs, reward, False, False, {}