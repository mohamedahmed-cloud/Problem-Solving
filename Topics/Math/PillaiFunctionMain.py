MAX=500005
phi=[i for i in range(MAX+1)]
pill=[0]*(MAX+1)
def compute_phi():
    global phi,MAX
    for i in range(2,MAX+1):
        if phi[i]==i:
            phi[i] -= 1
            for j in range(i*2,MAX+1,i):
                phi[j] -= int(phi[j] / i)

def compute_pill():
    global phi,pill
    for i in range(1,MAX+1):
        for j in range(i,MAX+1,i):
            pill[j] += i * phi[j // i]

compute_phi()
compute_pill()
