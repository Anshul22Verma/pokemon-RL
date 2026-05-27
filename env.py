import gymnasium as gym
import numpy as np
import socket
import cv2

class EmeraldEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = gym.spaces.Discrete(6)

        self.observation_space = gym.spaces.Box(
            low=0,
            high=255,
            shape=(240, 160, 3),
            dtype=np.uint8
        )

        self.sock = socket.socket()
        self.sock.connect(("127.0.0.1", 9999))

    def _get_obs(self):
        data = self.sock.recv(240*160*3)
        frame = np.frombuffer(data, dtype=np.uint8)
        return frame.reshape((240,160,3))

    def step(self, action):
        self.sock.send(bytes([action]))

        obs = self._get_obs()

        reward = 0.0
        done = False

        return obs, reward, done, False, {}

    def reset(self):
        return self._get_obs(), {}