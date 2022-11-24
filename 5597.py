import sys

input=sys.stdin.readline

student=[]

for _ in range(28):
    num=int(input())
    student.append(num)

all=[i for i in range(1,31)]

result=list(set(all)-set(student))

print(min(result),max(result))