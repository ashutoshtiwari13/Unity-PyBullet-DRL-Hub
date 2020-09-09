#  Ant PyBullet Environment - Soft Actor Critic (SAC)


Solving the environment  by usage of the *Soft Actor Critic* algorithm, see the summary of the basic paper [here]()

<img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Ant-PyBullet-Env-SAC/output/AntEnv-sim1.gif" height="400px" width="450px" hspace="20"/><img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Ant-PyBullet-Env-SAC/output/AntEnv-sim2.gif" height="400px" width="450px"/>

### Completion criteria
Solving the environment require an average total reward of over 2500 over 100 consecutive episodes.

### Environment parameters

max steps in episode:  1000   
state space dimension:  28   
action space dimension:  Box(8,)   

### Hyperparameters

batch size: 256    
learning rate:  0.0001

### Entropy regularization  

A central feature of SAC is [entropy regularization](https://spinningup.openai.com/en/latest/algorithms/sac.html).     
The major difference with common RL algorithms is training to maximize a trade-off between     
expected return and entropy, a measure of randomness in the policy. This has a close connection     
to the exploration-exploitation trade-off: increasing entropy results in more exploration,   
which can accelerate learning later on. It can also prevent the policy from prematurely    
converging to a bad local optimum.

### Reparameterization Trick

This trick makes training converge better due to lower variance. See function _sample()_ in the class  
_GaussianPolicy_ from _model.py_. The reparameterization trick allows us to rewrite the expectation over actions   
(which contains a pain point: the distribution depends on the policy parameters) into an [expectation over noise](https://spinningup.openai.com/en/latest/algorithms/sac.html).

### Training Score

The threshold score **2500** was achieved in the episode **1811**  after training **24 hours**.
<p align="center">
<img src="https://github.com/ashutoshtiwari13/Unity-DRL-Hub/blob/master/Ant-PyBullet-Env-SAC/output/plot_run1.png" height="380px" width="450px"/>
</p>
