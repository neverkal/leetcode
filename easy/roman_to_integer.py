"""
문제 : 로마 숫자로 계산하기, 숫자가 작은 기호가 큰수보다 앞에오는 경우 큰수 - 작은수
풀이 : dict에 로마숫자 정보를 담은 후 비교하여 각 숫자 합산
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        if 1 <= len(s) <= 15:
            sum_roman = 0
            idx_roman = 0

            while True:
                if idx_roman + 1 == len(s):
                    sum_roman += roman_integer[s[idx_roman]]
                    break
                elif idx_roman + 1 > len(s):
                    break

                before_roman = roman_integer[s[idx_roman]]
                after_roman = roman_integer[s[idx_roman + 1]]

                if before_roman < after_roman:
                    sum_roman += (after_roman - before_roman)
                    idx_roman += 2
                else:
                    sum_roman += roman_integer[s[idx_roman]]
                    idx_roman += 1

            return sum_roman
        else:
            return 0


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
