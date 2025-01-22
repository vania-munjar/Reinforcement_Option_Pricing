# Reinforcement_Option_Pricing

This project demonstrates the use of reinforcement learning to price American options using a Deep Q-Network (DQN) within a custom OpenAI Gym environment. Classical option pricing models such as Black-Scholes, Binomial Tree, and Barone-Adesi Whaley are implemented for comparison. The project ensures accurate simulation of the underlying asset's behavior using Geometric Brownian motion.

Project Features
Deep Q-Network (DQN):

Utilized TensorFlow to implement a reinforcement learning model for pricing American options.
Trained the DQN agent in a custom OpenAI Gym environment.
Custom OpenAI Gym Environment:

Simulates the behavior of the underlying asset using Geometric Brownian motion.
Incorporates option-specific parameters such as strike price, volatility, and risk-free rate.
Classical Option Pricing Models:

Compared DQN-based prices with models including:
Black-Scholes
Binomial Tree
Barone-Adesi Whaley
Used QuantLib for implementation of classical models.
Achieved a DQN price of $7.057 for the American option with an early exercise premium of $0.129.

# Key Results
DQN Pricing:

- Price: $7.057
- Early Exercise Premium: $0.129

# Classical Models Comparison:

Implemented Black-Scholes, Binomial Tree, and Barone-Adesi Whaley models for validation.
Future Work
Extend the DQN model to handle multi-dimensional state spaces for exotic options.
Explore other reinforcement learning techniques (e.g., PPO, SAC) for improved performance.
Optimize the Gym environment for faster convergence.

