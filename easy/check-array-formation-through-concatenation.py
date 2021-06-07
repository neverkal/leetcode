from typing import List

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        compare_arr = []
        check_pieces = [False for i in range(len(pieces))]

        for origin in arr:
            for idx, piece in enumerate(pieces):
                if origin in piece:
                    if check_pieces[idx] is False:
                        compare_arr.extend(piece)
                        check_pieces[idx] = True

        if arr == compare_arr:
            return True
        else:
            return False


sol = Solution()
print(sol.canFormArray(arr=[1,3,5,7], pieces=[[2,4,6,8]]))
