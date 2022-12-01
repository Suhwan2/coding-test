import sys

input=sys.stdin.readline

n,m,k=map(int,input().split())

chess=[]

for _ in range(n):
    chess.append(input().strip())

dpB=[[0]*(m+1) for _ in range(n+1)]
dpW=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        bb=ww=0
        if (i+j)%2==0:
            if chess[i-1][j-1]=='W':
                bb+=1
            else:
                ww+=1
        else:
            if chess[i-1][j-1]=='B':
                bb+=1
            else:
                ww+=1
        dpB[i][j]=dpB[i-1][j] + dpB[i][j-1] -dpB[i-1][j-1] +bb
        dpW[i][j]=dpW[i-1][j] + dpW[i][j-1] -dpW[i-1][j-1] +ww

result=100000000000000
for i in range(k,n+1):
    for j in range(k,m+1):
        b=dpB[i][j]-dpB[i-k][j]-dpB[i][j-k]+dpB[i-k][j-k]
        w=dpW[i][j]-dpW[i-k][j]-dpW[i][j-k]+dpW[i-k][j-k]
        result=min(b,w,result)

print(result)