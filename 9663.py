n=int(input())

row=[0]*n

def same(x):    
    for i in range(x):
        if row[i]==row[x] or abs(x-i) ==abs(row[i]-row[x]):
            return False
    return True
        
def dfs(x):
    if x==n:
        global count
        count+=1
        return
    for i in range(n):
        row[x]=i
        if same(x):
            dfs(x+1)
      
count=0
dfs(0)
print(count)


