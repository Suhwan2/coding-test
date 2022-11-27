import sys

input=sys.stdin.readline

n=int(input())

farm=[]

for _ in range(6):
    a,b=map(int,input().split())
    farm.append([a,b])

w=0
h=0
for i in range(len(farm)):
    if farm[i][0]==1 or farm[i][0]==2:
        if farm[i][1]>w:
            w=farm[i][1]
            w_idx=i

    elif farm[i][0]==3 or farm[i][0]==4:
        if farm[i][1]>h:
            h=farm[i][1]
            h_idx=i
s_w=abs(farm[(h_idx-1)%6][1]-farm[(h_idx+1)%6][1])
s_h=abs(farm[(w_idx-1)%6][1]-farm[(w_idx+1)%6][1])

print((w*h-s_w*s_h)*n)