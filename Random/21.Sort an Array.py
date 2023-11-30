class Solution:
    def solve(self,nums):
        def heapify(nums,size,i):
            largest=i
            l=2*i+1
            r=2*i+2
            if l<size and nums[l]>nums[largest]:
                largest=l
            if r<size and nums[r]>nums[largest]:
                largest=r
            if i!=largest:
                nums[largest],nums[i]=nums[i],nums[largest]
                heapify(nums,size,largest)
        def buildHeap(nums,size):
            startIndex=size//2 -1
            for i in range(startIndex,-1,-1):
                heapify(nums,size,i)
        def sortHeap(nums,size):
            buildHeap(nums,size)
            for i in range(size-1,0,-1):
                nums[i],nums[0]=nums[0],nums[i]
                heapify(nums,i,0)
        sortHeap(nums,len(nums))
        return nums
solve=Solution()
print(solve.solve([12, 11, 13, 5, 6, 7, ]))
