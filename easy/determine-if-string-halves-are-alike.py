class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        half_length = int(len(s) / 2)

        first_half = s[:half_length]
        last_half = s[half_length:]

        first_vowels = 0
        last_vowels = 0

        for i in range(half_length):
            if first_half[i - 1] in vowels:
                first_vowels += 1

            if last_half[i - 1] in vowels:
                last_vowels += 1

        if first_vowels == last_vowels:
            return True
        else:
            return False


sol = Solution()
print(sol.halvesAreAlike('AbCdEfGh'))
