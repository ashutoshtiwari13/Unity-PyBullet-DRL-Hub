
## Navigating Banana E
The agent is trained to navigate (and collect bananas!) in a large, square world.  

<img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/output/simulation.gif" height="425px" width="380px" hspace="20"/><img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/output/simulation-2.gif" height="425px" width="400px"/>

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting
a blue banana.  Thus, the goal of the agent is to collect as many yellow bananas as possible while
avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

### Completion criteria

The task is episodic, and in order to solve the environment, the agent must get an average score of +13
over 100 consecutive episodes.

### Environment

The environment is simulated by Unity application `Banana Env` lying in the subdirectory `Banana_env`
We start the environment as follows:

ON Mac :
```sh
env = UnityEnvironment(file_name="Banana.app")   
```
### Training sessions

We run several training sessions in according  to the variable _numb_of_trains_.
For each training session, the obtained weights are saved into the file 'weights_'+str(train_numb)+'.trn'.
We get files: _weights_0.trn_,  _weights_1.trn_,  _weights_2.trn_,  etc.

For each training session, we construct the **agent** with different parameters
and we run the *Deep-Q-Network* procedure **dqn** as follows:

  agent = **Agent**(state_size=37, action_size=4, seed=1, fc1_units=fc1_nodes, fc2_units=fc2_nodes)       
  scores, episodes = **dqn**(n_episodes = 2000, eps_start = epsilon_start, train_numb=i)  

### Training parameters

We experience the following parameters:  _fc1_units_, _fc2_units_,  _eps_start_.
At the end of each session these parameters together with the episode number (at which the training is finished)
are saved into the corresponding lists. These lists are used on the step of testing of weights.
For each training session,
 * _eps_start_ is played out as a random value from 0.988 to 0.955 with step 0.001,
 * _fc1_units_ is played out as a random value from 48 to 128 with step 16,
 * _fc2_inits_ is played out as a random value from fc1_units - 16 to fc1_units - 16 with step 8.

### Deep-Q-Network algorithm

The _Deep-Q-Network_ procedure **dqn** performs the **double loop**.
External loop (by _episodes_) is executed till the number of episodes reached the maximal number
of episodes _n_episodes = 2000_ or the _completion criteria_ is executed.
The environment _env_  is reset with the paarmeter _train_mode_=_True_.
For the completion criteria, we check  

  _np.mean(scores_window) >=13_,  

where _scores_window_ is the array of the type deque realizing  the shifting window of length <= 100.
The element _scores_window[i]_ contains the _score_ achieved by the algorithm on the episode _i_.


In the internal loop,  **dqn** gets the current _action_ from the **agent**.
By this _action_ **dqn** gets _state_ and _reward_ from Unity environment.
Then, the **agent** accept params _state,action,reward,next_state, done_
to the next training step. The variable _score_ accumulates obtained rewards.

### Agent

The class **Agent** is defined in `dqn_agent.py`. This is the well-known class implementing
the following mechanisms:

* Two Q-Networks (local and target) using the simple neural network.
* Replay memory (using the class ReplayBuffer)
* Epsilon-greedy mechanism
* Q-learning, i.e., using the max value for all possible actions
* Computing the loss function by MSE loss
* Minimize the loss by gradient descend mechanism using the ADAM optimizer

### Model Q-Network

Both Q-Networks (local and target) are implemented by the class
**QNetwork** lying in the file `model.py`. This class implements the simple
neural network with 3 fully-connected layers and 2
rectified nonlinear layers. This **QNetwork** is realized in the framework
of package **PyTorch**. The number of neurons of the fully-connected layers are
as follows:

 * Layer fc1,  number of neurons: **state_size** x **fc1_units**,
 * Layer fc2,  number of neurons: **fc1_units** x **fc2_units**,
 * Layer fc3,  number of neurons: **fc2_units** x **action_size**,

where **state_size** = 37, **action_size** = 8, **fc1_units** and **fc2_unit**
are the input params.

### Output of training

This is the typical output of training sessions:

 fc1_units:  48 , fc2_units:  32      
 train_numb:  1 eps_start:  0.992   
 Episode: 579, elapsed: 0:09:29.603803, Avg.Score: 13.00,  score 18.0, How many scores >= 13: 51, eps.: 0.10   
 terminating at episode : 579 avg.reward reached +13 over 100 episodes  
  <p align="center">
  <img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/output/scores_run2.png" height="425px" width="380px"/>
  </p>

 fc1_units:  80 , fc2_units:  88      
 train_numb:  2 eps_start:  0.992   
 Episode: 572, elapsed: 0:09:32.363203, Avg.Score: 13.00,  score 18.0, How many scores >= 13: 65, eps.: 0.10   
 terminating at episode : 572 avg.reward reached +13 over 100 episodes   

 <p align="center">
 <img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/output/scores_run3.png" height="425px" width="380px"/>
 </p>

### Credit

Most of the code is based on Udacity's DQN code.
