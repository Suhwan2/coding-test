while True:
    words=input()
    if words==".":
        break
    l=[]
    val=True
    for i in words:
        if i=='(':
            l.append(0)
        elif i=='[':
            l.append(1)
        elif i==')':
            if l and l[-1]==0:
                l.pop()
            else:
                val=False
                break
        elif i==']':
            if l and l[-1]==1:
                l.pop()
            else:
                val=False
                break
    
    if val and not l:
        print('yes')
    else:
        print('no')