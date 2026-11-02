class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in complement.keys():
                return [complement[comp], i]
            else:
                complement[nums[i]] = i

        