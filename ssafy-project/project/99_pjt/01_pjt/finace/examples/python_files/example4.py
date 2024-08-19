import pprint
import requests

# Openweather API 를 활용하여 서울의 현재 날씨 중 날씨에 대한 설명 정보만 출력하시오.

def get_seoul_weather():
    # OpenWeatherMap API 키
    api_key = '87246d75e1ce26e1392a087b3d1d88c5'

    # 검색 조건
    city = "Seoul,KR"

    # API 요청 URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    # API 요청 보내기
    json_response = requests.get(url).json()
    description = json_response['weather'][0]['description']
    return f'날씨 설명: {description}'
    


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_seoul_weather()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)