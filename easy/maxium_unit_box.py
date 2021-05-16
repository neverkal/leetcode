from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_cnt = 0
        total_unit = 0

        boxTypes.sort(key=lambda x: (-x[1]))

        for box in boxTypes:
            if box_cnt < truckSize:
                if box[0] == (truckSize - box_cnt):
                    avail_box = box[0]
                elif box[0] > (truckSize - box_cnt):
                    avail_box = truckSize - box_cnt
                else:
                    avail_box = box[0]

                box_cnt = box_cnt + avail_box
                total_unit = total_unit + (avail_box * box[1])
            else:
                break

        return total_unit


sol = Solution()
print(sol.maximumUnits(boxTypes=[[5,10],[2,5],[4,7],[3,9]], truckSize=10))
