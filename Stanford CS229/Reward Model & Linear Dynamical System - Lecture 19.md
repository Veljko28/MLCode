
## Finite Horizon MDP

A Finite Horizon Markov Decision Process (MDP) is a specific type of MDP where the decision-making problem has a fixed time horizon, meaning that the agent makes decisions over a limited number of time steps or stages. Unlike an infinite horizon MDP, where the decision process continues indefinitely, a finite horizon MDP has a defined endpoint after a certain number of time steps.

In a Finite Horizon MDP, the agent's objective is typically to maximize the cumulative rewards or expected return within the specified time horizon. The agent needs to consider both immediate rewards and future rewards within the remaining time steps to make optimal decisions.


## Linear Quadratic Regulation (LQR)

Linear Quadratic Regulation (LQR) is a classical control technique used to design optimal control policies for linear systems subject to quadratic cost functions. It is widely used in control theory and engineering to achieve optimal control of linear dynamical systems, such as robotic systems, aircraft, and industrial processes.

The LQR problem aims to find a control policy that minimizes a quadratic cost function while ensuring that the system follows a desired trajectory or setpoint. The cost function typically includes terms for the deviation of the system state from the desired state (tracking error) and the control effort required to achieve the desired behavior.

The general form of the LQR cost function is:

J = ∫ \[x^T(t) * Q * x(t) + u^T(t) * R * u(t)] dt


## Linearizing a non-linear model

Linearizing a non-linear model is a technique used in control systems engineering and related fields to approximate a non-linear system as a linear one around a specific operating point or equilibrium. By linearizing the system, we can use linear control techniques like PID controllers or Linear Quadratic Regulators (LQR) to design controllers for the non-linear system.

The linearization process involves two main steps:

1. Finding the operating point: The first step is to find an operating point or equilibrium for the non-linear system. This is a state at which the system is stable, and the derivative of the states with respect to time is zero (i.e., dx/dt = 0). The operating point represents the desired behavior of the system.

2. Linear approximation: Once the operating point is determined, the non-linear system can be approximated as a linear one by computing the linearization around the operating point. This is achieved by finding the Jacobian matrix, which represents the partial derivatives of the system's state-space equations with respect to the states and control inputs.