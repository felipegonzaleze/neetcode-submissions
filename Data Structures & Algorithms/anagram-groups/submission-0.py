class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = []
        anagram_groups = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            anagram_groups[tuple(count)].append(word)
        for group in anagram_groups:
            groups.append(anagram_groups[group])
        return groups
