asc = [1,2,3,4,5,6,7,8]
dec = sorted(asc,reverse=True)
data = list(map(int,input().split()))
if data == asc:
    print('ascending')
elif data == dec:
    print('descending')
else:
    print('mixed')

