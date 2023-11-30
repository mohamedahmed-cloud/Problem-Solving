#!/usr/bin/env python3
# find missing x
l = [1, 2, 1, 5,2]
ans = 0
for i in l:
	ans ^= i
print(ans)

# Find odd or even.
x = 3
y = 6
if y & 1:
	print("odd")
else:
	print("Even")

# << Left Shift && >> Right Shift
# << add 0 to right
# >> remove first bit
print(10<<1)

print(120000000000000000000000001>>1 == 120000000000000000000000001 // 2) # true
# Get specific bit
def getBit(num, indx):
	return (1 << indx) & num != 0
def setBit(num, indx):
	return (1 << indx) | num
def flipBit(num, indx):
	return (1 << indx) ^ num
print(flipBit(4, 2))


# helpful techinques
# X-1 is very important!
A = 72 # 1001000

A - 1 # => 71 # 1000111 ( remove first bit "1" an make all bits before it with 1 )

A & (A-1) #=> 10000000  # remove first "1" bit from right

A & ~(A-1) # get all bits from right until first "1" bit
