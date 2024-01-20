from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.adjacent_matrix = defaultdict(set)
        self.n = len(isConnected)

        for i in range(self.n):
            tmp = []
            for j in range(self.n):
                tmp.append(j + 1) if isConnected[i][j] else 0
            self.create(tmp)
        # print(self.adjacent_matrix)
        token = defaultdict(set)
        all = set()
        def dfs(key, value):
            if value:
                for i in value:
                    if i not in all:
                        token[key].add(i)
                        all.add(i)
                        dfs(key, self.adjacent_matrix[i])
            else:
                token[key]


        for keys, values in self.adjacent_matrix.items():
            all.add(keys)
            dfs(keys, values)
        # print(token)
        return len(token)

    def create(self, connected):
        n = len(connected)
        for i in range(n):
            self.adjacent_matrix[connected[i]]
            for j in range(i + 1, n):
                self.adjacent_matrix[connected[i]].add(connected[j])
                self.adjacent_matrix[connected[j]].add(connected[i])

    

slv = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(slv.findCircleNum(isConnected))

# another solution using Union Find
