# 라이브러리 : 남들이 만들어 놓은 코드를 가져다 쓰자 !
# 데이터를 가져오는 python 라이브러리(패키지) : requests
# 파이썬 패키지 관리 : pip 
    # 설치 : pip install (패키지이름)
    # 목록 확인 : pip list


# import requests

# url = "https://fakestoreapi.com/carts"
# data = requests.get(url).json()
# print(data)


# ## .get() url을 가져와라.
# ##  .json() : 딕셔너리로 형태를 변환해준다.

# ## API  
# # 코드에 대한 요청을 해석하고 
# # Data를 검색한 후 데이터를 전달한다.


## pprint() : 데이터 이쁘게 보기

import requests
import json
import pprint

api_key = 'e9b0e3f0da29b0e93cc62e595098b7ca'

# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()
pprint.pprint(data['name'])



# 날씨 요약 정보 : 'clear sky'가 출력되도록 해보자 !
pprint.pprint(data['weather'][0]['description'])
pprint.pprint(data.get('weather')[0].get('description'))


# 추가 공부 과제    # 차이점이 뭔지 ?
data['weather']
data.get['weather']

















































# ##################### 코드 ##################
# from pprint import pprint as print 
# import requests
# import json

# # 위도: 35.095776, 경도: 128.854736

# city = 'Busan'
# lat = 35.09
# lon = 128.85
# apiKey = 'e9b0e3f0da29b0e93cc62e595098b7ca'
# lang = 'kr'
# units = 'metric'

# # 위도 경도로 날씨 출력하기
# # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}" 

# # 도시 이름으로 날씨 출력하기
# url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"

# result = requests.get(url)
# result = json.loads(result.text)

# degree_k = result['main']['temp']
# degree_c = degree_k - 273.15

# description = result['weather'][0]['main']

# print(f'{city} / {degree_c:.2f}°C / {description}')


# ######################코드 ############################