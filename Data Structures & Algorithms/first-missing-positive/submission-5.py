class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positives = []
        for num in nums:
            if num > 0:
                positives.append(num)
        positives.sort()
        for i in range(len(positives)):
            if positives[0] > 1:
                return 1
            if positives[i] + 1 not in positives:
                return positives[i] + 1
        return 1