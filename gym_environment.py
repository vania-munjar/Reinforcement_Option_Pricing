import gym
import numpy as np

class OptionPricingEnv(gym.Env):
    def __init__(self):
        super(OptionPricingEnv, self).__init__()
        self.observation_space = gym.spaces.Box(low=0, high=np.inf, shape=(1,), dtype=np.float32)
        self.action_space = gym.spaces.Discrete(2)  # Hold or Exercise
        
        self.S = 100  # Initial stock price
        self.strike = 100
        self.T = 1.0  # Time to maturity
        self.r = 0.05  # Risk-free rate
        self.sigma = 0.2  # Volatility
        self.dt = 0.01
        self.current_time = 0
    
    def reset(self):
        self.S = 100
        self.current_time = 0
        return np.array([self.S], dtype=np.float32)
    
    def step(self, action):
        if action == 1:  # Exercise
            reward = max(self.S - self.strike, 0) * np.exp(-self.r * self.current_time)
            done = True
        else:  # Hold
            reward = 0
            self.S *= np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt) * np.random.normal())
            self.current_time += self.dt
            done = self.current_time >= self.T
        
        return np.array([self.S], dtype=np.float32), reward, done, {}

    def render(self, mode="human"):
        print(f"Stock Price: {self.S}, Time: {self.current_time}")

