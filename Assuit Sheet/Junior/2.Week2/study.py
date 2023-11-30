def test(n):
        if n>0:
            print(n)
            test(n-1)
            print(n)
test(10)