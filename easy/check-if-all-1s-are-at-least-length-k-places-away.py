from typing import List

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        check_ones = [i for i, v in enumerate(nums) if v == 1]

        for i, one in enumerate(check_ones):
            if i + 1 >= len(check_ones):
                break
            elif (check_ones[i + 1] - one) - 1 < k:
                return False

        return True


sol = Solution()
print(sol.kLengthApart(nums = [1,0,0,1,0,1], k = 2))
