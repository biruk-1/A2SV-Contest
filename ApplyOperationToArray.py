from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):  
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        zeroCount = 0
        for j in range(len(nums) - 1):
            if nums[j] == 0:
                if nums[j + 1] != 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                else:
                    zeroCount += 1

        for k in range(zeroCount):
            nums.remove(0)
            nums.append(0)

        return nums
