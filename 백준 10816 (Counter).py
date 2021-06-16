import sys
from collections import Counter

N = int(sys.stdin.readline()) # 10
array = list(map(int, sys.stdin.readline().split())) # 6 3 2 10 10 10 -10 -10 7 3
M = int(sys.stdin.readline()) # 8 
data = list(map(int, sys.stdin.readline().split())) # 10 9 -5 2 3 4 5 -10
array.sort() # -10 -10 2 3 3 6 7 10 10 10 

array = Counter(array)
for i in data:
    print(array[i], end=" ")