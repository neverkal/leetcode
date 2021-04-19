"""
문제 : 정수형 범위에서 입력받은 값을 거꾸로 출력
풀이 :
- 정수형 범위 체크
- 입력받은 정수를 str으로 형변환하여 출력
- 음수의 경우 앞에 부호 추가
"""
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31 - 1 or x <= -2**31:
            return 0
        else:
            str_int = str(x)
            if x >= 0:
                str_reverse = str_int[::-1]
            else:
                temp = str_int[1:]
                temp2 = temp[::-1]
                str_reverse = "-" + temp2

            if int(str_reverse) >= 2 ** 31 - 1 or int(str_reverse) <= -2 ** 31:
                return 0
            else:
                return int(str_reverse)


sol = Solution()
print(sol.reverse(x=-23940235920340923040239))
