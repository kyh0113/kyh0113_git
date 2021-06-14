import sys 
N = int(sys.stdin.readline())

array=[]
for i in range(N):
    data = sys.stdin.readline().split()
    array.append((int(data[0]), int(data[1])))

array.sort()
# array = sorted(array, key =lambda x:x[1])

# print(array)

for i in array:
    print(i[0], i[1])

