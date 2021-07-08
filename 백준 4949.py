while (1):
    s=input().rstrip()

    if s=='.':
        break

    stack=[]
    answer=True

    for i in range(len(s)):
        if s[i] =='(' or s[i]=='[':
            stack.append(s[i])
        elif s[i] ==')':
            if len(stack) == 0 or stack[-1] == '[':
                answer=False
                break
            elif stack[-1] =='(':
                stack.pop()
                continue
        
        elif s[i]==']':
            if len(stack) ==0 or stack[-1] =='(':
                answer=False
                break
            elif stack[-1] =='[':
                stack.pop()
                continue
            
    if answer==True:
        print('yes')
    else:
        print('no')

# [(]) <- 이런건 'no' 
