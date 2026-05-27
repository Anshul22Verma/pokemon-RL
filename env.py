import gymnasium as gym
from gymnasium import spaces

import socket
import numpy as np
import cv2


ACTIONS = [
    "NONE",
    "A",
    "B",
    "UP",
    "DOWN",
    "LEFT",
    "RIGHT"
]


class EmeraldEnv(gym.Env):

    def __init__(self):

        super().__init__()

        self.sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        print("Connecting to BizHawk...")

        self.sock.connect(("127.0.0.1", 9999))

        print("Connected!")

        self.action_space = spaces.Discrete(
            len(ACTIONS)
        )

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(160, 240, 3),
            dtype=np.uint8
        )

    def _get_frame(self):

        data = b""

        while len(data) < 160 * 240 * 3:
            packet = self.sock.recv(4096)
            data += packet

        frame = np.frombuffer(
            data[:160*240*3],
            dtype=np.uint8
        )

        frame = frame.reshape(
            (160, 240, 3)
        )

        return frame

    def reset(self, seed=None, options=None):

        obs = self._get_frame()

        return obs, {}

    def step(self, action):

        command = ACTIONS[action]

        self.sock.send(
            command.encode()
        )

        obs = self._get_frame()

        reward = 0.01

        terminated = False

        truncated = False

        info = {}

        return (
            obs,
            reward,
            terminated,
            truncated,
            info
        )