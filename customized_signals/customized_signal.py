# Gym stuff
import gymnasium as gym
import gym_anytrading

# Stable baselines - rl stuff
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import A2C

# Processing libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import argparse
import yfinance as yf
import quantstats as qs

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="CustomizedSignal",
        description="Train RL for Trading",
        epilog="Example: py customized_signal.py --name AMD --window-size 10",
    )
    parser.add_argument(
        "--name",
        nargs=1,
        help="Name of the Stock",
    )
    parser.add_argument(
        "--window-size",
        nargs=1,
        help="Window Size",
    )
    
    args = parser.parse_args()

    df = yf.Ticker(args.name[0])
    df = df.history(period="max")
    df = df.loc['2020-01-01':, ['Open', 'High', 'Low', 'Close', 'Volume']]

    print(df.head())
    # TRAIN_WINDOW_SIZE = 10
    # TRAIN_SIZE = df['2020-01-01':'2022-12-31'].shape[0]
    # TRAIN_ENV_FRAME_BOUND = (10, TRAIN_SIZE)

    # SMA_PERIOD = 10

    # TEST_ENV_FRAME_BOUND = (TRAIN_SIZE + 1, df.shape[0])
    # TEST_WINDOW_SIZE = 10


 