
l = [3, 1, 8, 2, 5,3,3,5,7,54,2,5,3,2,5,45,6,3,4,2,3,34,5,23,5,76,7,79,12,37,3,6,1,3,8,5,0,7,4,7,2,1,6,3]

def func(A):
    L = [1] * len(A)
    for i in range(1,len(L)):
        subproblemas = [L[k] for k in range(i) if A[k] < A[i]]
        L[i] = 1 + max(subproblemas, default=0)
    return max(L, default=0)


func(l)