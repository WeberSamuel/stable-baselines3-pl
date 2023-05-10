import os

from stable_baselines3_pl.a2c import A2C
from stable_baselines3_pl.common.utils import get_system_info
from stable_baselines3_pl.ddpg import DDPG
from stable_baselines3_pl.dqn import DQN
from stable_baselines3_pl.her.her_replay_buffer import HerReplayBuffer
from stable_baselines3_pl.ppo import PPO
from stable_baselines3_pl.sac import SAC
from stable_baselines3_pl.td3 import TD3

# Read version from file
version_file = os.path.join(os.path.dirname(__file__), "version.txt")
with open(version_file) as file_handler:
    __version__ = file_handler.read().strip()


def HER(*args, **kwargs):
    raise ImportError(
        "Since Stable Baselines 2.1.0, `HER` is now a replay buffer class `HerReplayBuffer`.\n "
        "Please check the documentation for more information: https://stable-baselines3.readthedocs.io/"
    )


__all__ = [
    "A2C",
    "DDPG",
    "DQN",
    "PPO",
    "SAC",
    "TD3",
    "HerReplayBuffer",
    "get_system_info",
]