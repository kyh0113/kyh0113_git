import sys
N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort() # 이진탐색으로 풀려면 사전에 정렬이 되어 있어야함

M = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

def binary_search(array, data, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] == data:
            return True
        elif array[mid] > data:
            end = mid-1
        elif array[mid] < data:
            start = mid+1
    return None

for i in data:
    result = binary_search(array, i, 0, N-1)
    if result == True:
        print("yes", end=" ")
    else:
        print("no", end=" ")




