from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_money = 0

        for account in accounts:
            sum_account_money = 0
            for money in account:
                sum_account_money += money

            if max_money < sum_account_money:
                max_money = sum_account_money

        return max_money


sol = Solution()
print(sol.maximumWealth(accounts=[[2,8,7],[7,1,3],[1,9,5]]))
