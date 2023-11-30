class Solution:
    def solve(self,time,totalTrips):
        l=1
        r=totalTrips*max(time)
        def binarySeach(l,r):
            while r>l:
                t=(l+r)//2
                if check(t)<totalTrips:
                    l=t+1
                elif check(t)>=totalTrips:
                    r=t
            return r
        def check(t):
            currentTrip=0
            for i in time:
                currentTrip+=(t//i)
            return currentTrip
        return binarySeach(l,r)
    
solve=Solution()
print(solve.solve([5,10,10],9))