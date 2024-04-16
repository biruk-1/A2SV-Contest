class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        myArray = []
        n = len(arr)
        while n > 1:
            m = max(arr[:n])
            max_index = arr.index(m)
            if max_index != n - 1:
                k = max_index + 1
                arr[:k] = reversed(arr[:k])
                myArray.append(k)
                arr[:n] = reversed(arr[:n])
                myArray.append(n)
            n -= 1
        return myArray
