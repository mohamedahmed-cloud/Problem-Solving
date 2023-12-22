def query(BITTree,i): 
	s = 0
	i = i+1
	while i > 0: 
		s += BITTree[i] 
		# 2's complement then & with orignal then - => to find child
		i -= i & (-i) 
	return s 


def update(BITTree , n , i ,v): 
	i += 1
	while i <= n: 
		BITTree[i] += v
		# 2's complement then & with orignal then + => to find parent
		i += i & (-i) 


def construct(arr, n): 
	BITTree = [0]*(n+1)
	for i in range(n): 
		update(BITTree, n, i, arr[i]) 

	return BITTree 


# Driver code to test above methods 
freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9] 
BITTree = construct(freq,len(freq)) 
print("Sum of elements in arr[0..5] is " + str(query(BITTree,5))) 
freq[3] += 6
update(BITTree, len(freq), 3, 6) 
print("Sum of elements in arr[0..5]"+
					" after update is " + str(query(BITTree,5))) 


