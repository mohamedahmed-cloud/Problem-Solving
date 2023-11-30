from typing import Optional, List
from collections import defaultdict, deque

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in adjacentPairs:
            graph[i[1]].append(i[0])
            graph[i[0]].append(i[1])
        print(graph)

        ans = deque()
        for key, value in graph.items():
            if len(value) == 1:
                ans.append(key)
                ans.append(value[0])
                break
                
        n = len(adjacentPairs)
        token = set(ans)
        cnt = 2

        while cnt <= n:
            curr = graph[ans[-1]]
            for j in curr:
                if j not in token:
                    token.add(j)
                    ans.append(j)
                    cnt += 1
        return ans  



