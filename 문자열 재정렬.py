# 문자열 담을 변수와 숫자를 담을 변수를 따로 만들기

data = input()
result=[] # 문자열 담기
value=0 # 숫자 다 더한 값 저장

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort() # 알파벳 정렬

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value!=0:
    # result.append(value) <- 이렇게 append할 수 없음 int인 value를 str로 변경해야함
    result.append(str(value))
    
print(''.join(result))