- To know the nunmber of divisior for any number.
1. find the square root of it.
2. if square root is perfect then the number of divisor is odd else even 
- `code`
    ```py
    def NumOfDivisor(n):
        if n < 1:
            return
        root_n = int(math.sqrt(n))
        

        if root_n**2 == n:
            print('Odd')
        else:
            print('Even')

    ```
-------------

- To find the specific number in array that can give me specific number.
1. make for all element in array `&` if i number in array & specific number = element in array. 
2. then this element must be count in the element that consist of it.

-----------

- UpSolving Problem:
- [ ] [link](https://codeforces.com/contest/1779) - Hello 2023 - problem C.

- [ ]  [link](https://codeforces.com/contest/1768) - Round 842 - Problem D.

