n=int(input())

l=list(map(int,input().split()))
oper=list(map(int,input().split()))

    
def dfs(x,result):
    bakcup=result
    if x==(n-1):
        global min,max
        if result>max:
            max=result
        if result < min:
            min=result
        return 0
    for i in range(len(oper)):
        if oper[i]>0:
            if i==0:
                result+=l[x+1]
            elif i==1:
                result-=l[x+1]
            elif i==2:
                result*=l[x+1]
            else :
                if result<0:
                    result= -((-result)//l[x+1])
                else:
                    result= result//l[x+1]
            oper[i]-=1
            dfs(x+1,result)

            result=bakcup
            oper[i]+=1


min=1000000000
max=-1000000000
dfs(0,l[0])

print(max)
print(min)