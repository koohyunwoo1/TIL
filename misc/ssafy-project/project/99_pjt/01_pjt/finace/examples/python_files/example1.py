import pprint
import requests


# Openweather API 를 활용하여 특정 지역의 "현재 날씨"에 대한 정보를 출력하세요.
# 서울의 위도:37.56, 경도:126.97

def get_seoul_weather():
    # OpenWeatherMap API 키
    api_key = '87246d75e1ce26e1392a087b3d1d88c5'

    # 서울의 위도
    lat = 37.56
    # 서울의 경도
    lon = 126.97

    # API 요청 URL
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

    # API 요청 보내기
    response = requests.get(url).json()
    return response


if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_seoul_weather()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)
