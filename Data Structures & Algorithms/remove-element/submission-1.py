class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        for num in nums:
            if num != val:
                nums[count] = num
                count += 1
        return count