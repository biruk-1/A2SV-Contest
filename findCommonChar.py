class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        myArray = []
        counter = Counter(words[0])
        for j in counter:
            minMum = counter[j]
            for k in range(1,len(words)):
                minMum = min(minMum,words[k].count(j))
            myArray.extend(minMum*j)
        return myArray

