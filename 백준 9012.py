import sys

def stack_push(stack, value):
    stack.append(value)

def stack_pop(stack):
    last=stack.pop()
    return last

T=int(sys.stdin.readline())

for i in range(T):
    stack=[]
    OK=True
    s=sys.stdin.readline()
    for j in range(len(s)):
        if s[j]=='(':
            stack_push(stack, '(')
        elif s[j]==')':
            if len(stack)==0:
                OK=False
                break
            last = stack_pop(stack) #위 함수에서 return을 안해주면 last값은 none이 된다
            if last== '(':
                continue
    if len(stack) !=0:
        OK =False
    if OK==True:
        print("YES")
    else:
        print("NO")

