i, j = 0 , 0 
result = []
arr1 = [6]
arr2 = [1,3,4]

def isValid(i, j):
    print(i,j)
    return i < len(arr1) and j < len(arr2)

while isValid(i, j):
    if arr1[i] <= arr2[j]:
        result.append(arr1[i])
        i += 1
    elif arr1[i] > arr2[j]:
        result.append(arr2[j])
        j += 1

for _ in range(i,len(arr1)):
    result.append(arr1[_])

for _ in range(j, len(arr2)):
    result.append(arr2[_])

print(result)