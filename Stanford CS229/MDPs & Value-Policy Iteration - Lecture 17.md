
## Bellman's Equation

Bellman's equation is a fundamental equation in the field of dynamic programming and reinforcement learning. It plays a crucial role in solving Markov Decision Problems (MDPs) and finding optimal policies in uncertain and sequential decision-making scenarios.

The Bellman's equation is a recursive relationship that expresses the value function of a state in terms of the expected value of the immediate reward and the value of the next state. It is defined as follows:

V(s) = max\[Σ P(s'|s, a) * (R(s, a, s') + γ * V(s'))]

By solving Bellman's equation, one can obtain the optimal value function V*(s), which represents the maximum expected cumulative reward from each state under the optimal policy. The optimal policy π*(s) can then be derived from the optimal value function, specifying the best action to take in each state to achieve the highest cumulative reward over time.

## Value Iteration & V*

The value iteration algorithm iteratively updates the value function of each state until it converges to the optimal value function. At each iteration, the value function of each state is updated using Bellman's optimality equation. The algorithm continues to iterate until the value function no longer significantly changes, indicating that it has converged to the optimal solution.

The steps of the value iteration algorithm are as follows:

1. Initialize the value function: Start by initializing the value function for all states. Typically, all values are set to zero or some arbitrary initial values.

2. Value update: In each iteration, update the value function for each state s based on Bellman's optimality equation. 

3. Convergence check: After updating the value function for all states, check if the values have significantly changed. If the values have not changed beyond a certain threshold, the algorithm has converged, and the optimal value function has been found.
 
4. Policy extraction: Once the value iteration converges and the optimal value function is obtained, the optimal policy can be derived from the value function by selecting the action that maximizes the value function in each state.

## Policy Iteration 

An optimal policy, in the context of Markov Decision Problems (MDPs) and Reinforcement Learning, is a decision-making strategy that maximizes the expected cumulative reward or expected return over time. It represents the best possible way for an agent to select actions in different states to achieve its goals in a dynamic and uncertain environment.

In an MDP, the agent's objective is typically to find the policy that leads to the highest total reward over the long run. This optimal policy is often denoted by π*, and it is the one that provides the most favorable sequence of actions to maximize the expected sum of rewards.

Formally, the optimal policy π* is defined as:

π*(s) = argmax Σ P(s'|s, a) \* (R(s, a, s') + γ * V*(s'))

Here γ is a decision factor which is lower than 1 (eg. 0.98) and is multiplied which each action to the power of its index. eg. γ\* R(s1) + γ^2\*R(s2)  + γ^3\*R(s3)...

## Exploration vs Exploitation Problem

It refers to the dilemma faced by an agent when making choices between exploring unknown options (exploration) and exploiting known options to maximize its rewards (exploitation).

In Reinforcement Learning, an agent learns to make decisions in an uncertain environment by interacting with it. At each step, the agent can take different actions, leading to different states and receiving rewards based on its actions. The agent's objective is to learn an optimal policy that maximizes its cumulative rewards over time.

Exploration: Exploration involves trying out different actions, even if they are not known to yield high rewards. By exploring new actions and states, the agent can gather more information about the environment and discover potentially better strategies. In the early stages of learning or when the agent is uncertain about the environment, exploration is crucial to avoid getting stuck in suboptimal policies.

Exploitation: Exploitation involves choosing actions that are known to yield high rewards based on the agent's current knowledge. Exploiting known actions can lead to immediate gains and allow the agent to follow the learned optimal policy. Once the agent has accumulated enough knowledge about the environment, exploitation becomes essential to maximize the rewards.

The trade-off between exploration and exploitation arises because, in many cases, trying new actions and exploring uncharted territory may lead to temporarily lower rewards before potentially finding better solutions. On the other hand, sticking to what is known and exploiting the best actions may limit the agent from finding even better strategies.

## ε-greedy 

A simple approach where the agent chooses the best-known action with high probability (exploitation) and explores a random action with a small probability (exploration). For example going with exploitation 0.9 or 90% of the time and going in a new direction 0.1 or 10% of the time. This way we can explore more routes without wasting too much computation power. We can even decrease the **ε (the probability of taking a new route)** by 0.01 so that we waste even less computation power. 
