"""
문제 : 입력한 수를 거꾸로 불러도 동일한 수가 나오는 경우 Ture 아닌 경우 False
풀이 : 입력 한 수를 거꾸로 만든뒤 비교
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if -2**31 <= x <= 2**31 - 1:
            str_int = str(x)
            str_reverse = str_int[::-1]

            try:
                return True if int(str_reverse) == x else False
            except ValueError:
                return False
        else:
            return False


sol = Solution()
print(sol.isPalindrome(10))
