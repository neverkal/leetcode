class Solution:
    def numberOfSteps(self, num: int) -> int:
        divide_cnt = 0
        divide_num = num

        while divide_num > 0:
            if divide_num % 2 == 0:
                divide_num = int(divide_num / 2)
            else:
                divide_num = divide_num - 1

            divide_cnt += 1

        return divide_cnt


sol = Solution()
print(sol.numberOfSteps(8))
