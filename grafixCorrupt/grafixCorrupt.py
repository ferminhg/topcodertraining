class grafixCorrupt:
    def selectWord(self, dictionary, candidate):
        topSimil = candidatePos = -1
        for i in range(len(dictionary)):
            simil = self.calculateSimil(dictionary[i], candidate)
            if simil > topSimil :
                topSimil = simil
                candidatePos = i

        return candidatePos

    def calculateSimil(self, word, candidate):
        value = -1
        for i in range(len(word)):
            if (word[i] == candidate[i]):
                value += 1
        return value


gc = grafixCorrupt()
assert gc.selectWord(["cat", "cab", "lab"], "dab") == 1
assert gc.selectWord(["cat", "cab", "lab"], "lag") == 2