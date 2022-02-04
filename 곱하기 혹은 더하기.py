# '0'혹은 '1'인 경우 곱하기 보다는 더하기를 수행해야 더 큰 수를 만들 수 있음
data = input() # str형태로 입력

first = int(data[0])

for i in range(1, len(data)):
    # 맨 앞 숫자 또는 다음 숫자들 중 숫자 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if first <=1 or num <=1:
        first +=num
    else:
        first *=num

print(first)