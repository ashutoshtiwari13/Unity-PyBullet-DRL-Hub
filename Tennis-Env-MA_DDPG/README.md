## Multi-Agent Continous Control (MA DDPG) - Tennis Env

The projetc uses the [Tennis](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#tennis) environment, where two agents control rackets to bounce ball over a net.     
If an agent hits a ball over net, the agent receives a reward of +0.1. If an agent lets a ball hit the ground or hits the ball   
out of bounds, the agent receives a reward of -0.01. Thus, the goal of each agent is to keep the ball in play.    
The observation space is 24-dimensional consisting of 8 variables corresponding to the position and velocity  
of the ball and racket. Each agent receives its own, local observation. Two continuous actions are available, corresponding
to movement toward (or away from) the net, and jumping. The accompanying research paper can be found [here](https://arxiv.org/pdf/1706.02275.pdf).

<img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Tennis-Env-MA_DDPG/output/Tennis.gif" height="425px" width="380px" hspace="20"/><img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Tennis-Env-MA_DDPG/output/sim2.jpg" height="425px" width="400px"/>


### Maddpg Environment

The environment is simulated by Unity application _Tennis.app_ lying in the subdirectory _Tennis_Windows_x86_64_.
We start the environment as follows:

On Mac:
```sh
      env = UnityEnvironment(seed=seed, file_name="Tennis.app")
```

## Completion criteria
The task is episodic, and in order to solve the environment, the agents must get an **average score** of +0.5
(over 100 consecutive episodes, after taking the maximum over both agents).       

Multi-agent environment requires the training of two separate agents, and the agents need to collaborate under certain situations (like don’t let the ball hit the ground) and compete under other situations (like gather as many points as possible). Just doing a simple extension of single agent RL by independently training the two agents does not work very well because the agents are independently updating their policies as learning progresses. And this causes the environment to appear
non-stationary from the viewpoint of any one agent.

### Train the Agent

```sh
   Run the notebook tennis_run1.ipynb_
```
   [1] import UnityEnvironment    
   [2] env = UnityEnvironment(seed=seed, file_name="Tennis.app")   # create environment        
   [3] Environments contain _brains_ which are responsible for deciding the actions of their associated agents.     
       We check for the first brain available.      
   [4] Examine the State and Action Spaces. We get the information frame as follows:   

     Number of agents: 2   
     Size of each action: 2   
     There are 2 agents. Each observes a state with length: 24    
     The state for the first agent looks like:
     [ 0.          0.          0.          0.          0.          0.     
       0.          0.          0.          0.          0.          0.   
       0.          0.          0.          0.         -6.65278625 -1.5   
      -0.          0.          6.83172083  6.         -0.          0.        ]     

   [5]  Create _env_info_ and _maddpg agent_:

     env_info = env.reset(train_mode=True)[brain_name]      
     agent = maddpg_agent(num_agents=2, state_size=24, action_size=2)   

   [6]  Define and run the main function _train_ :

     scores_total, scores_global = train(maddpg, env, dir_chkpoints, n_episodes=1700)  

   [7]  Print graph of scores_total (blue bars) over all episodes, and  scores_global  
        (the line 'Avg on 100 episodes' - orange points)    
        The environment was solved in **1302 episodes**,  at this point the **Average Score** is achieved to **+0.5**,    
        see `tennis_run1.ipynb`.   


### Train History

At **1600 episode** the **Average Score** is achived to **+1.14**.  
<img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Tennis-Env-MA_DDPG/output/plot_1600episodes.png" height="425px" width="380px"/>
</p>
