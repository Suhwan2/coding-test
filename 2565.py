import sys

n=int(sys.stdin.readline())

p=[]
for _ in range(n):
    a=list(map(int,sys.stdin.readline().split()))
    p.append(a)

def check():
    dp=[0]*n
    for i in range(n):
        for j in range(i+1,n):
            if (p[i][0]-p[j][0])*(p[i][1]-p[j][1])<0:
                dp[i]+=1
                dp[j]+=1
    return max(dp),dp.index(max(dp))

cnt=0

while True:
    a,b=check()

    if a==0:
        break
    p[b][0]=0
    p[b][1]=0
    cnt+=1
print(cnt)
