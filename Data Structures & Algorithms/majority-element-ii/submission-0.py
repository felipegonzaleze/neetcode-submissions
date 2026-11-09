class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        times = (len(nums) / 3)
        freq = defaultdict(int)
        result = []
        print(times)
        for num in nums:
            freq[num] += 1
        for k in freq:
            print(k, freq[k])
            if freq[k] > times:
                result.append(k)
        return result