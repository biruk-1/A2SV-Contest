class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numbers = sorted(nums)
        myArray = []
        for num in nums:
            myArray.append(numbers.index(num))
        return myArray
