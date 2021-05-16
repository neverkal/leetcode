class Solution:
    """
    문제 : stone에 포함되어 있는 jewels의 개수 출력
    jewels의 길이는 1과 같거나 크다, stones는 길이가 50과 같거나 작다
    jewels, stones 는 모두 영어
    jewles의 각 문자는 유일하다
    """
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels) >= 1 and len(stones) <= 50:
            sum_jewels = 0

            for jewel in jewels:
                sum_jewels += stones.count(jewel)

            return sum_jewels
        else:
            exit()


sol = Solution()
print(sol.numJewelsInStones(jewels="aA", stones="aAAbbbb"))
