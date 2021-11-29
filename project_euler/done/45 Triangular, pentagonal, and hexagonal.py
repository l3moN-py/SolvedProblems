T = [n*(n+1)/2 for n in range(1,100000)]
P = [p*(3*p-1)/2 for p in range(1,100000)]
H = [n*(2*n-1) for n in range(1,100000)]

def common_member(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)
    if (a_set & b_set & c_set):
        print(a_set & b_set & c_set)
    else:
        print("No common elements")



common_member(T, P, H)
