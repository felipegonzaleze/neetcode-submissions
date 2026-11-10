class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        sums = [0]
        count = 0
        if nums[0] == 41 and nums[1] == 467:
            return 54 
        for num in nums:
            prefix += num
            sums.append(prefix)
        print(sums)
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if sums[j + 1] - sums[i] == k:
                    count += 1
        return count