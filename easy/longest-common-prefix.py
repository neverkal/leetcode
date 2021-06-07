from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare_str = strs[0]
        temp_str = ""

        if len(strs) == 1:
            return compare_str
        else:
            for i, char in enumerate(compare_str):
                for strs_idx in range(1, len(strs)):
                    if len(strs[strs_idx]) > i and strs[strs_idx][i] == char:
                        continue
                    else:
                        return temp_str

                temp_str = "".join([temp_str, char])

            return temp_str


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
