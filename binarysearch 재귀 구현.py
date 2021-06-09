import sys

def binary_search(array, target, start, end):
    if start > end: # 탐색하고자 하는 범위에 데이터가 존재하지 않으면
        return None
    mid = (start + end) // 2
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    elif array[mid] == target:
        return mid

n, target = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else :
    print(result + 1)