# LunarLander Environment -Deep Deterministic Policy Gradient

Solving the environment require an average total reward of over **200** on 100 consecutive episodes.If lander moves away from landing pad it loses reward back. Episode finishes if the lander crashes or comes to rest, receiving additional -100 or +100 points. Each leg ground contact is +10. Firing main engine is -0.3 points each frame. Firing side engine is -0.03 points each frame. Landing outside landing pad is possible. Fuel is infinite, so an agent can learn to fly and then land on its first attempt.

<img src="https://github.com/ashutoshtiwari13/Unity-PyBullet-DRL-Hub/blob/master/LunarLander-Env-DDPG/output/LL-sim1.gif" height="400px" width="450px" hspace="20"/><img src="https://github.com/ashutoshtiwari13/Unity-PyBullet-DRL-Hub/blob/master/LunarLander-Env-DDPG/output/LL-sim2.gif" height="400px" width="450px"/>

### Actions in LunarLanderContinuous   

Any action is the vector of two real numbers **{_v1_, _v2_}**, such that **-1 < _v1_, _v2_ < 1**.    
The first coordinate **_v1_** controls main engine: if **-1 < _v1_ <= 0** the main engine off.     
The values  **0 < _v1_ < 1** are corresponding to the throttle from **50%** to **100%** power, i.e., **power = 50(_v1_+1)**.     
The second coordinate **_v2_** controls left/right engines:        
Values  **-1 < _v2_ <= -0.5** fire the left engine; values  **0.5 <= _v2_ <  1** fire the right engine,    
Values  **-0.5 < _v2_ 0.5** left and right engines off.   

### Training

Score **200** achieved in **2560** episodes.
<p align="center">
<img src="https://github.com/ashutoshtiwari13/Unity-PyBullet-DRL-Hub/blob/master/LunarLander-Env-DDPG/output/plot_run1.png" height="380px" width="450px"/>
</p>

Learning rate for actor = 1e-3, for critic = 1e-3
