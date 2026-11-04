class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums) / 2
        d = {}
        for num in nums:
            d[num] = 1 + d.get(num, 0)
            if d[num] > times:
                return num
        