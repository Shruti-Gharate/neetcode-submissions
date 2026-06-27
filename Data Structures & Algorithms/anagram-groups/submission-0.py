from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for words in strs:
            anagram = ''.join(sorted(words))
            final[anagram].append(words)

        return list(final.values())