def find(arr):
    
    arr.sort()
    ans = 0
    for i in range(1, len(arr)):
        ans += arr[i] * arr[i -1]
      
    return ans
  
find([2, 5, 7, 4, 8])
