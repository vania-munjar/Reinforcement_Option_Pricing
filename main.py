from gym_environment import OptionPricingEnv
from dqn_agent import DQNAgent
from classical_models import calculate_classical_prices
from utils import plot_results

def main():
    # Initialize environment
    env = OptionPricingEnv()
    
    # Initialize DQN Agent
    agent = DQNAgent(state_size=env.observation_space.shape[0], action_size=env.action_space.n)
    
    # Training the agent
    episodes = 500
    rewards = []
    for episode in range(episodes):
        state = env.reset()
        total_reward = 0
        done = False
        
        while not done:
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward
            
            if done:
                print(f"Episode: {episode + 1}/{episodes}, Reward: {total_reward}")
                rewards.append(total_reward)
        
        agent.replay(batch_size=32)
    
    # Save the trained model
    agent.save("dqn_model.h5")
    
    # Classical model comparison
    classical_prices = calculate_classical_prices()
    print("Classical Model Prices:", classical_prices)
    
    # Plot results
    plot_results(rewards, classical_prices)

if __name__ == "__main__":
    main()
