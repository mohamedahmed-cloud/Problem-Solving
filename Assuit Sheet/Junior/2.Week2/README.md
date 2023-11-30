## queue
#### First Type
```py
# First In Frist Out it's like list
import queue
q=queue.Queue()
arr=[1,2,3,4,5,6]
for i in arr:
    q.put(i)
print(q)
while not q.empty():
    print(q.get())
```
#### Second Type
```py
# Make queue last in first out
import queue
q=queue.LifoQueue()
arr=[1,2,3,4,5,6]
for i in arr:
    q.put(i)
print(q)
while not q.empty():
    print(q.get())
```
#### Thrid Type 
```py
# Priority queue[ To print number form lower to higher ]
# [smaller number is a higher priority]
import queue
q=queue.PriorityQueue()
arr=[7,6,5,4,3,2,1]
for i in arr:
    q.put(i)
print(q)
while not q.empty():
    print(q.get())
```
#### Notes 
- You can add any type of data in queue like number ,string,tuple and so on.
---
## deque in python 
- main deque
```py
from collections import deque
d=deque("hello")
print(d)
print(list(d))
```
- add element in deque 
```py
    from collections import deque
    # add element into deque
    # To end
    d=deque("")
    d.append('4')
    d.append(8)
    print(d)
    # To first
    d=deque('')
    d.appendleft('mo')
    d.appendleft('90')
    print(d)
```
- Removing element in deque 
```py
    from collections import deque
    # removine element from the deque
    # remove last element
    d=deque('mohamed')
    # remove last element
    d.pop()
    # remove first element
    d.popleft()
    print(d)
    # To clear
    d.clear()
    print(d)
```
- add iterable element to deque 
```py
    # Add iterable element to deque
    d=deque()
    d.extend('ahmed')
    # add to the end of the deque
    d.extend([1,2,3,4,5,6,7])
    # add to the begining of the deque
    d.extendleft([1,2,3,4])
    print(d)
```
- Rotate and Shift
```py
    # Rotate or shift
    d=deque()
    d.extend([1,2,3,4,5,6,7])
    # Shift right
    d.rotate(-1)
    print(d)
    # Shift Left
    d=deque()
    d.extend([1,2,3,4,5,6,7])
    d.rotate(1)
    print(d)
    # we can rotate by -1 and -2 and so on.
    # We can rotate by 1 and 2 and so on.
```
- Give maxlen to deque 
```py
    # give maxlen for deque
    d=deque([1,2,3,4,5],maxlen=5)
    # d.append()
    print(d)
    d.append(9)
    print(d)
    # we can't change maxlen after initialize it like
    # d.maxlen=9 can't do this
    print(d.maxlen)
```
- Reverse deque 
```py
    # reverse
    d=deque("mohamed")
    d.reverse()
    print(d)
```
---
## Stack

```py
    # Stack 
    # stack in python is an empty list 
    # when we want to append an element in it use .append()
    # when we want to remove an element in it use .pop()
    # Like
    data=[]
    data.append(5)
    data.append(6)
    data.append(7)
    data.append(8)
    last=data.pop()
    print(last)
    print(data)

```
## Queue
- we can use queue like stack note the difference
```py
    # First in first out
    data=[]
    data.append(5)
    data.append(6)
    data.append(7)
    data.append(8)
    last=data.pop(0)
    print(last)
    print(data)
```
---
## bisect module
- used to Insert element in sorted array
```py
import bisect
arr=[1,1,2,3,4,5,6,7,9]
key=7
# Here he will insert key in sorted array in it's position but the key is repeat in array it will insert key on the right

print(bisect.bisect(arr,key))
# Here he will insert key in sorted array in it's position but the key is repeat in array it will insert key on the left
print(bisect.bisect_left(arr,key))
# to append element to array
bisect.insort(arr,key)
```
---
```py
    # itertools to find permuation of element.
    import sys,math,itertools
    arr=[1,2,3,4,5]
    a=itertools.permutations(arr)
    for i in a:
        print(i)
```
---
## priority Queue
- [Video](https://www.youtube.com/watch?v=wGSQ486Y4sc)
- `general info`
```py
# Time to add and remove number from heap is log
# heapq => allow us to use heap in python.
import heapq
'''
heap has two heap type 
    min heap => the min element in the back of tree.
    max heap => the max element in the front of tree.
represent of binary tree.
first element   i
child =>  2*i+1   2*i+2  and so on.
'''
```
- `min-heap`
```py
    data=[10,20,43,1,3,7,50,2,3]
    heapq.heapify(data) # to turn list to min heap
    # when you remove element from heap the structure of heap will change to make a truly proiority queue.
    heapq.heappop(data) #pop the first node in the tree.
    # to copy data from array
    arr=data[:] # or data.copy()
    # To add data to heap
        # heapq.heappush(heap,element)
    heapq.heappush(data,6)
    print(data)
    # make element sign is reverese in heap.
    reverse_data=data[:]
    reverse_data=[-x for x in data]
    heapq.heapify(data)
    print(reverse_data)
```
- `max-heap`
```py
    max_heap=[10,20,43,1,3,7,50,2,3]
    heapq._heapify_max(max_heap) # to turn list to max heap.
    print(max_heap)
    heapq._heappop_max(max_heap) # remove element from max heap
    print(max_heap)
``` 
- `merge two list in heap`
```py
    # To merge list in heap
    l1=[10,9,8,20,40]
    l2=[1,4,7,19,90]
    all=heapq.merge(l1,l2)
    print(list(all))
```

