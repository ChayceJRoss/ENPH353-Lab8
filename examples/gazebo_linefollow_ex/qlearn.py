import random
import pickle


class QLearn:
    def __init__(self, actions, epsilon, alpha, gamma):
        self.q = {}
        self.epsilon = epsilon  # exploration constant
        self.alpha = alpha      # discount constant
        self.gamma = gamma      # discount factor
        self.actions = actions

    def loadQ(self, filename):
        '''
        Load the Q state-action values from a pickle file.
        '''
        try: 
            with open(filename+".pickle", "rb") as f:
                self.q = pickle.load(f)
                print("Loaded file: {}, with data {}.".format(filename+".pickle", self.q))
        except:
            print("File not found, starting with empty Q dictionary.")
            self.q = {}
        # TODO: Implement loading Q values from pickle file.



    def saveQ(self, filename):
        '''
        Save the Q state-action values in a pickle file.
        '''
        try:
            with open(filename+".pickle", "wb") as f:
                pickle.dump(self.q, f)
        except:
            print("Could not write to file: {}".format(filename+".pickle"))
        # TODO: Implement saving Q values to pickle and CSV files.

        print("Wrote to file: {}".format(filename+".pickle"))

    def getQ(self, state, action):
        '''
        @brief returns the state, action Q value or 0.0 if the value is 
            missing
        '''
        return self.q.get((state, action), 0.0)

    def chooseAction(self, state, return_q=False):
        '''
        @brief returns a random action epsilon % of the time or the action 
            associated with the largest Q value in (1-epsilon)% of the time
        '''
        # TODO: Implement exploration vs exploitation
        #    if we need to take a random action:
        #       * return a random action
        #    else:
        #       * determine which action has the highest Q value for the state 
        #          we are in.
        #       * address edge cases - what if 2 actions have the same max Q 
        #          value?
        #       * return the action with highest Q value
        #
        # NOTE: if return_q is set to True return (action, q) instead of
        #       just action

        # THE NEXT LINES NEED TO BE MODIFIED TO MATCH THE REQUIREMENTS ABOVE 
        choice = random.choice(self.actions)
        if random.random() >= self.epsilon:
            max = 0
            for action in self.actions:
                if self.getQ(state, action) > max:
                    max = self.getQ(state, action)
                    choice = action
        if return_q:
            return choice, self.q
        return choice

    def learn(self, state1, action1, reward, state2):
        '''
        @brief updates the Q(state,value) dictionary using the bellman update
            equation
        '''
        # TODO: Implement the Bellman update function:
        #     Q(s1, a1) += alpha * [reward(s1,a1) + gamma* max(Q(s2)) - Q(s1,a1)]
        # 
        # NOTE: address edge cases: i.e. 
        # 
        # Find Q for current (state1, action1)
        # Address edge cases what do we want to do if the [state, action]
        #       is not in our dictionary?
        # Find max(Q) for state2
        # Update Q for (state1, action1) (use discount factor gamma for future 
        #   rewards)

        # THE NEXT LINES NEED TO BE MODIFIED TO MATCH THE REQUIREMENTS ABOVE
        if self.getQ(state1, action1) == 0:
            self.q[(state1,action1)] = 0
        else:
            max2 = 0
            for action in self.actions:
                for action in self.actions:
                    if self.getQ(state2, action) > max2:
                        max2 = self.getQ(state2, action)
            self.q[(state1,action1)] += self.alpha * (reward + self.gamma * (max2 - self.q[(state1,action1)]))

