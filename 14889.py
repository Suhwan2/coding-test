n=int(input())
l=[]

for _ in range(n):
    num=list(map(int,input().split()))
    l.append(num)

def cal(team):
    s_team=set(team)
    s_all=set([i for i in range(n)])

    team_2=list(s_all-s_team)
    result_1=0
    result_2=0
    for i in range(n//2):
        for j in range(i+1,n//2):
            n_1=team[i]
            n_2=team[j]
            result_1+=(l[n_1][n_2]+l[n_2][n_1])

    for i in range(n//2):
        for j in range(i+1,n//2):
            n_1=team_2[i]
            n_2=team_2[j]
            result_2+=(l[n_1][n_2]+l[n_2][n_1])
    return abs(result_1-result_2)
def dfs(x):
    if x==(n//2)-1:
        result=cal(team)    
        global min
        if min > result:
            min=result
        return 0
    for i in range(n):
        if len(team)==0 or team[x]<i :
            team.append(i)
            dfs(x+1)
            team.pop()
team=[]
min=100000000
dfs(-1)

print(min)