class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        N = len(nums)
        r = nums[0] + nums[1] + nums[N-1]
        t = abs(target - r)
        for i in range(N):
            s, e = i + 1, N - 1
            while s < e:
                tmpSum = nums[i] + nums[s] + nums[e]
                if t > abs(target - tmpSum):
                    r = tmpSum
                    t = abs(target - tmpSum)

                if tmpSum < target:
                    s = s + 1
                else:
                    e = e - 1
                    
        return r
