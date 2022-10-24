e=input()

result=0
b=False
prev=''
for i in range(len(e)):
    if e[i]=='-':
        if b and prev:
            result-=int(prev)
            prev=''
        elif not b and prev:
            result+=int(prev)
            prev=''
        b=True

    elif e[i]=='+':
        if b:
            result-=int(prev)
        else:
            result+=int(prev)
        prev=''
    else:
        prev+=e[i]
    
    if i==len(e)-1:
        if b:
            result-=int(prev)
        else:
            result+=int(prev)

print(result)