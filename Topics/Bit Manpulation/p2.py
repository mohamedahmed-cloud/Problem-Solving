#!/usr/bin/env python3

# Smallest power of 2 greater than or equal to n
def small_power(num):
	while num > 0 and  (num & (num -1)):
		num += 1
	return num
num = 10**9
print(small_power(num))