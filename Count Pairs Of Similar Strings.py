class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordSet = collections.defaultdict(set)
        for indx, word in enumerate(words):
            wordSet[indx] = set(word)
        
        ans = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(wordSet[i].symmetric_difference(wordSet[j])) == 0:
                    ans += 1
        return ans
