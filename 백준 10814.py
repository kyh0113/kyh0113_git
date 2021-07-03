import sys
N=int(sys.stdin.readline())

l=[]
for i in range(N):
    age, name = (sys.stdin.readline().split())
    age = int(age)
    name = str(name)
    l.append((age, name))
    
l.sort(key=lambda x:x[0]) # age로 정렬

for i in l:
    print(i[0], i[1])
