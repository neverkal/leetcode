from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        check_positive_num = 1
        check_positive_count = 0
        check_positive_list = []

        while check_positive_count < k:
            if check_positive_num not in arr:
                check_positive_count += 1
                check_positive_list.append(check_positive_num)

            check_positive_num += 1

        return check_positive_list[k-1]


sol = Solution()
print(sol.findKthPositive(arr=[1,2,3,4,5], k=4))
