from typing import Optional, List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def find(c):
            count = 0
            total = 0
            
            for i in weights:
                if c >= (total + i):
                    total += i
                    # print(total)

                else:
                    total = i
                    count += 1


            # print(count)

            count +=1 if total != 0 else 0
            # print(count,  c, total)

            return True if count <= days else False
        

        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = left + (right - left) // 2
            # print(left, mid, right)
            if find(mid):
                right = mid
            else:
                left = mid + 1

        return left