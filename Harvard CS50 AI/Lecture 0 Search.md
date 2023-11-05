## Search

An agent is the thing that is interacting with the environment and performing actions based on what it's policy is.

State is the current position of given data. If we were trying to go trough a maze the state would be the current location of the agent in this maze. 
Initial State is the first position for the given agent.

An action is a function that given a certain state and a transition would output the next state or all possible states from the given state.

A goal test is a test that tries to get to the desired state (of which there could be one or many) in any possible way. We use this to determine weather it's even possible to get to the desired/goal state.

In certain situations like driving a car there is a cost for us choosing one route over another. For this we use the path cost function, which will go trough the graph and find the path that costs the least.

dfs,bfs, dijkstra...

