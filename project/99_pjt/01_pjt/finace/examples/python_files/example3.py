import pprint
import requests

# Openweather API 를 활용하여 서울의 온도에 대해 출력하시오.

def get_seoul_weather():
    # OpenWeatherMap API 키
    api_key = '87246d75e1ce26e1392a087b3d1d88c5'

    # 검색 조건
    city = "Seoul,KR"

    # API 요청 URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # API 요청 보내기
    json_response = requests.get(url).json()

    # 키 값 출력해보기
    # print(json_response.keys())

    # 캘빈 온도 출력
    temperature = json_response['main']['temp']
    print(f"캘빈 온도: {temperature}K")

    # 섭씨 온도는 캘빈 - 273.15
    temperature_celsius = temperature - 273.15
    print(f"섭씨 온도: {temperature_celsius:.2f}˚C")



if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_seoul_weather()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    # pprint.pprint(result)