
#Code from Banana-Env-DQN
class ReplayBuffer:
    """Fixed-size buffer to store experience tuples."""

    def __init__(self, batch_size, n_agent, seed):
        """Initialize a ReplayBuffer object.
        Params
        ======
            batch_size (int): size of each training batch
        """
        self.memory = []
        self.batch_size = batch_size
        self.seed = np.random.seed(seed*2018)

    def add(self, trajectories):
        """Add new trajectory to memory."""
        self.memory.extend(trajectories)

    def sample(self):
        """Randomly sample a batch of experiences from memory."""
        states, actions, log_probs_old, returns, advantages = map(lambda x: torch.cat(x, dim=0), zip(*self.memory))
        advantages = (advantages - advantages.mean()) / advantages.std()

        indices = np.arange(states.size()[0])
        np.random.shuffle(indices)
        indices = [indices[div*self.batch_size: (div+1)*self.batch_size] for div in range(len(indices) // self.batch_size + 1)]

        result = []
        for indice in indices:
            if len(indice) >= self.batch_size / 2:
                indice = torch.Tensor(indice).long().to(device)
                result.append([states[indice], actions[indice], log_probs_old[indice], returns[indice], advantages[indice]])
        return result

    def reset(self):
        self.memory = []

    def __len__(self):
        return len(self.memory)
