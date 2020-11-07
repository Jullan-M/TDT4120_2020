def rod_cut_bottom_up(p, n):
    r = [0]*(n+1)

    for j in range(1, n+1):
        q = -1
        for i in range(1, j+1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    return r[n]

def rod_cut_memoized_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            q = max(q, p[i-1] + rod_cut_memoized_aux(p, n - i, r))
    r[n] = q
    return q

def rod_cut_memoized(p, n):
    r = [-1]*(n+1)
    return rod_cut_memoized_aux(p, n, r)


p = [1,5,8,9,10,17,17,20,24,30]
n = 9
print("---- Bottom-up ----")
print(f"Max profit with n = {n}: {rod_cut_bottom_up(p,n)}")
print()
print("---- Memoized ----")
print(f"Max profit with n = {n}: {rod_cut_memoized(p,n)}")