import bisect

numbers = [4, 7, 10, 13]

insertion_point = bisect.bisect_right(numbers, 10) 
print(insertion_point)
