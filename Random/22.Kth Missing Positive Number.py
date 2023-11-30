class Solution:
    def solve(self,arr,k):
        freq=[0]*(int(1e3 *2)+5)
        for i in arr:
            freq[i]+=1

        # print(freq[:10])
        for i,value in enumerate(freq[1:]):
            if value==0:
                if k==1:
                    return i+1
                k-=1
            
solve=Solution()
print(solve.solve([1,2,3,4,5],2000-5))
