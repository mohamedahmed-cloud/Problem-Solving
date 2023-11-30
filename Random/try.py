def printArray(arr, n):
    print(len(arr))
    print(*arr)

def hashing(table, tsize, arr, N):
    for i in range(N):
        hv = arr[i] % tsize


        if (table[hv] == -1):
            table[hv] = arr[i]

        else:
            for j in range(tsize):
                t = (hv + j * j) % tsize
                if (table[t] == -1):
                    table[t] = arr[i]
                    if arr[i]==20:
                        print(*table)
                        print(t)
                        exit()
                    break

    printArray(table, N)

if __name__ == "__main__":
    arr = [8,2,7,18,15,19,23,15,20,16]
    N = len(arr)
    print(N)
    L =13

    hash_table = [-1] * L
    hashing(hash_table, L, arr, N)
