def solve(s):
    s.strip()
    l=s.split()
    return len(l[-1])
print(solve("ab abbda     "))