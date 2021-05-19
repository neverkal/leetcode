class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        check_num = 1

        for i in range(n + 1):
            if i > 1:
                if (check_num * 2) == i:
                    nums.append(nums[check_num])
                elif ((check_num * 2) + 1) == i:
                    nums.append(nums[check_num] + nums[check_num + 1])
                    check_num += 1
            else:
                nums.append(i)

        return max(nums)


sol = Solution()
print(sol.getMaximumGenerated(3))
