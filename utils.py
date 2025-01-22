import matplotlib.pyplot as plt

def plot_results(rewards, classical_prices):
    plt.plot(rewards, label="DQN Rewards")
    plt.axhline(y=classical_prices["Black-Scholes"], color="r", linestyle="--", label="Classical Price")
    plt.legend()
    plt.xlabel("Episodes")
    plt.ylabel("Rewards/Price")
    plt.title("Reinforcement Learning vs Classical Models")
    plt.show()
