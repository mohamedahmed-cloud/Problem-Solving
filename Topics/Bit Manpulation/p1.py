#!/usr/bin/env python3

# power of two or not
def is_power_of_two(num):
	return num > 0 and not (num & (num -1))

num = 8
print(is_power_of_two(num))