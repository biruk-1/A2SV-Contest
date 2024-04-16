class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums = sorted(nums)
        myArray = []
        for i in range(n):
            if nums[i] == target:
                myArray.append(i)
        return myArray
