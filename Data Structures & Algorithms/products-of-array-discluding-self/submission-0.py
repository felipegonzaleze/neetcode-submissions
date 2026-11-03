class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            total = 1
            for j in range(len(nums)):
                if nums[i] == nums[j] and nums[i] == 0:
                    continue
                total *= nums[j]
            if nums[i] == 0:
                products.append(total)
            else:
                total /= nums[i]
                products.append(int(total))
        return products 