class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i

        for i in range(len(nums)):
            if (dict.get(target-nums[i]) is not None) & (i != dict.get(target-nums[i])):
                return [i, dict.get(target-nums[i])]
