class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        elements = []
        while k > 0:
            inf = float("-inf")
            highest_idx = 0
            # recorrer todos los nums
            for f in freq:
                # si la frecuencia es mayor que -inf
                if freq[f] >= inf:
                    highest_idx = f
                    inf = freq[f]
            elements.append(highest_idx)
            freq.pop(highest_idx)
            k -= 1
        return elements