class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        uniques = set()
        j = 0
        for i in range(len(nums)):
            if nums[i] not in uniques:
                uniques.add(nums[i])
            elif nums[i] in uniques:
                while nums[j] != nums[i]:
                    j += 1
                if i != j and abs(i - j) <= k:
                    return True
                else:
                    j += 1
        print(i, j)
        return False