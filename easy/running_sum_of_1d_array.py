from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            check_idx = i + 1

            if check_idx == len(nums):
                break

            nums[check_idx] += nums[check_idx - 1]

        return nums


sol = Solution()
print(sol.runningSum(nums=[1, 2, 3, 4]))
