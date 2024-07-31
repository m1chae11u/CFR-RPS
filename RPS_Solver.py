# RPS_Solver.py

import random

class RPS_Solver:
    def __init__(self):
        self.ROCK, self.PAPER, self.SCISSORS = 0, 1, 2
        self.NUM_ACTIONS = 3
        self.regretSum = [0.0] * self.NUM_ACTIONS # list of accumulated regrets for not playing each action
        self.strategy = [0.0] * self.NUM_ACTIONS # list to store the current mixed strategy
        self.strategySum = [0.0] * self.NUM_ACTIONS # list to accumulate the strategies over time for averaging
        self.oppStrategy = [0.4, 0.3, 0.3]  # example opponent strategy

    def getStrategy(self):
        normalizingSum = 0.0
        for a in range(self.NUM_ACTIONS):
            self.strategy[a] = self.regretSum[a] if self.regretSum[a] > 0 else 0.0
            normalizingSum += self.strategy[a]
        for a in range(self.NUM_ACTIONS):
            if normalizingSum > 0:
                self.strategy[a] /= normalizingSum
            else:
                self.strategy[a] = 1.0 / self.NUM_ACTIONS
            self.strategySum[a] += self.strategy[a]
        return self.strategy

    def getAction(self, strategy):
        r = random.random()
        a = 0
        cumulativeProbability = 0.0
        while a < self.NUM_ACTIONS - 1:
            cumulativeProbability += strategy[a]
            if r < cumulativeProbability:
                break
            a += 1
        return a

    def train(self, iterations):
        actionUtility = [0.0] * self.NUM_ACTIONS
        for i in range(iterations):
            strategy = self.getStrategy()
            myAction = self.getAction(strategy)
            otherAction = self.getAction(self.oppStrategy)

            actionUtility[otherAction] = 0
            actionUtility[(otherAction + 1) % self.NUM_ACTIONS] = 1
            actionUtility[(otherAction + self.NUM_ACTIONS - 1) % self.NUM_ACTIONS] = -1

            for a in range(self.NUM_ACTIONS):
                self.regretSum[a] += actionUtility[a] - actionUtility[myAction]

    def getAverageStrategy(self):
        avgStrategy = [0.0] * self.NUM_ACTIONS
        normalizingSum = sum(self.strategySum)
        for a in range(self.NUM_ACTIONS):
            if normalizingSum > 0:
                avgStrategy[a] = self.strategySum[a] / normalizingSum
            else:
                avgStrategy[a] = 1.0 / self.NUM_ACTIONS
        return avgStrategy