import requests
import json

city = 'Seoul'
apikey = "827fc262c7e57a1ea32e397b40c622b5"
lang = "kr" # 한국어로 출력하기 위함
units = "metric" # 화씨를 섭씨로 출력하기 위함

# f-string : 파이썬 문자열 포매팅
api = f"""http://api.openweathermap.org/data/2.5/\
weather?q={city}&appid={apikey}&lang={lang}&units={units}""" # lang과 units라는 파라미터를 추가(&)함
# 위 api주소로 직접 Openwheathermap api에 요청을 보내고 응답 받아오기

response = requests.get(api)
# print(response.text) # str (json)

# data = json.loads(response.text) # 응답값을 json으로 변경
# # print(type(data)) # dict

# print(data["name"], "의 날씨입니다.")
# print("날씨는", data["weather"][0]["description"], "입니다.") # 하나의 리스트 안에 있음 [0]
# print("현재 온도는", data["main"]["temp"], "입니다.") 
# print("하지만 체감 온도는", data["main"]["feels_like"], "입니다.") 
# print("최저 기온은", data["main"]["temp_min"], "입니다.")
# print("최고 기온은", data["main"]["temp_max"], "입니다.")
# print("습도는", data["main"]["humidity"], "입니다.")
# print("기압은", data["main"]["pressure"], "입니다.")
# print("풍향은", data["wind"]["deg"], "입니다.")
# print("풍속은", data["wind"]["speed"], "입니다.")

data = response.text
# print(data)

print("날씨는", data["weather"][0]["description"], "입니다.")