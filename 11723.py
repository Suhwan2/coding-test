from sys import stdin as st

m=int(input())

s=set()
for _ in range(m):
    word=st.readline().strip()
    if word=='all':
        s=set([i for i in range(1,21)])
    elif word=='empty':
        s=set()
    else:
        word=word.split()
        a,b=word[0],int(word[1])

        if a=='add':
            s.add(b)
        elif a=='remove':
            if b in s:
                s.remove(b)
        elif a=='check':
            if b in s:
                print('1')
            else:
                print('0')
        elif a=='toggle':
            if b in s:
                s.remove(b)
            else:
                s.add(b)
