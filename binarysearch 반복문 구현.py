import sys

n, target = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) //2
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid-1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        elif array[mid] < target:
            start = mid+1
    return None



result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else : 
    print(result + 1)