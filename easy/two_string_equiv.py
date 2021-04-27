from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if 1 <= len(word1) and len(word2) <= 10**3:
            word1_join = "".join(word1)
            word2_join = "".join(word2)

            if word1_join == word2_join:
                return True
            else:
                return False
        else:
            return False


sol = Solution()
print(sol.arrayStringsAreEqual(word1=["abc", "d", "defg"], word2=["abcddefg"]))

