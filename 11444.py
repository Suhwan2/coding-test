from sys import stdin as st

n=int(st.readline())
p=1000000007

def cal(A,B):
    n=len(A[0])
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                C[i][j]+=A[i][l]*B[l][j]%p
    return C
def square(mat,n):
    if n==1:
        return mat
    tmp=square(mat,n//2)
    if n%2==0:
        return cal(tmp,tmp)
    else:
        return cal(cal(tmp,tmp),mat)
A=[[1,1],[1,0]]
result=square(A,n)

print(result[0][1]%p)