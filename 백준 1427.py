N=input()
l=list(map(int, str(N)))
a=sorted(l, reverse=True)
for i in a:
    print(i, end="")
