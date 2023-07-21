
## Questions to ask when things go wrong

1. Improve Model/Simulator?
2. Modify Reward Function R?
3. Modify RL Algorithm?

## Diagnostics

1. If π flies well in simulation, but not in real life, then the problem is in the simulator. Otherwise:
2.  Let π_human be the human control policy. If Vπ(s0) < Vπ_human(s0), then the problem is in the reinforcement learning algorithm. (Failing to maximize the expected payoff.)
3. Otherwise, then the problem is in the cost function. (Maximizing it doesn't correspond to good autonomous flight.) 

## Policy Search Algorithms

**Policy search algorithms** are a class of optimization techniques used in Reinforcement Learning (RL) to find an optimal policy for an agent in a given environment. Unlike model-based methods that try to estimate the dynamics of the environment, policy search algorithms directly optimize the policy without explicitly modeling the environment.

The main idea behind policy search is to search for the policy parameters that result in the best performance, measured by the expected cumulative reward or any other objective function. These algorithms iteratively update the policy parameters to improve the agent's performance through interactions with the environment.

Gradient Ascent: **Policy Gradient** methods use gradient ascent to update the policy parameters in the direction that maximizes the expected cumulative reward. The gradient is estimated using samples obtained from interactions with the environment.


## Reinforce Algorithm

The Reinforce algorithm, also known as the **Monte Carlo Policy Gradient (MCPG)** algorithm, is a popular policy gradient method used in Reinforcement Learning (RL) to optimize the policy of an agent. It is a model-free algorithm, meaning that it directly estimates the policy without explicitly modeling the environment.

The Reinforce algorithm is based on the idea of estimating the gradient of the expected cumulative reward with respect to the policy parameters. By iteratively updating the policy parameters in the direction of the estimated gradient, the agent can learn an optimal policy that maximizes the expected cumulative reward.


## Partially observable MDP (POMDP)

A **Partially Observable Markov Decision Process** (POMDP) is an extension of the classic Markov Decision Process (MDP) that deals with situations where the agent's observations do not fully reveal the underlying state of the environment. In a POMDP, the agent has access to noisy or incomplete observations, making it uncertain about the true state of the environment.

In a standard MDP, the agent directly observes the current state of the environment and selects actions based on this complete information. However, in a POMDP, the agent receives partial or noisy observations, which are typically generated from the true state according to an observation model.

The agent's objective in a POMDP is to find an optimal policy that maximizes the expected cumulative reward, given the partial observations and the hidden states. Solving POMDPs is generally more challenging than standard MDPs due to the uncertainty in the observations and the need to maintain a belief over possible hidden states.