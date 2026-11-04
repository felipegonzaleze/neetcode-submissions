class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return max(d, key = d.get)
        