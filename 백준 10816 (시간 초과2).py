import sys
from collections import Counter

N = int(sys.stdin.readline()) # 10
array = list(map(int, sys.stdin.readline().split())) # 6 3 2 10 10 10 -10 -10 7 3
M = int(sys.stdin.readline()) # 8 
data = list(map(int, sys.stdin.readline().split())) # 10 9 -5 2 3 4 5 -10
array.sort() # -10 -10 2 3 3 6 7 10 10 10 

def binary_search(array, d, start, end): 
    while start <= end:
        mid = (start + end) //2
        if array[mid] == d:
            return array[start : end+1].count(d)
        elif array[mid] > d:
            end = mid-1
        elif array[mid] < d:
            start = mid+1
    return 0
    
dic={}
for i in range(len(data)):
    dic[i] = binary_search(array, data[i], 0, N-1)
    print(dic[i], end=" ")
