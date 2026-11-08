class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = suffix = 1
        products = []
        for num in nums:
            products.append(prefix)
            prefix *= num
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]
        return products