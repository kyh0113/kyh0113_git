import sys
N=int(sys.stdin.readline())

word=[]
for i in range(N):
    st=input()
    word.append(st)

set_word  = list(set(word))

sort_word=[]

for i in set_word:
    sort_word.append((len(i), i))

result = sorted(sort_word) # 길이를 기준으로 정렬

for i, j in result:
    print(j)