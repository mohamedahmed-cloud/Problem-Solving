from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (x[1], x[0]))
        res = [] * len(people)
        for i in people:
            cnt = i[1]
            indx = 0
            for val, rnk in res:
                if i[0] <= val:
                    cnt -= 1
                if cnt < 0: break
                indx += 1
            print(res)
            res.insert(indx, i)
        print(res)

slv = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(slv.reconstructQueue(people))

# another solution


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0], x[1]))

        res = []
        for val, rnk in people:
            res.insert(rnk, [val, rnk])
        return res

slv = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(slv.reconstructQueue(people))