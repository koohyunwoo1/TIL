import pprint
import requests

# 응답 중 정기예금 상품들의 옵션 리스트를 출력하도록 구성합니다.
# 이 때, 원하는 데이터만 추출하여 새로운 리스트를 만들어 반환하는 함수를 작성하시오.
# [힌트] 아래와 같은 순서로 데이터를 출력하며 진행합니다.
# 1. 응답을 json 형식으로 변환합니다.
# 2. key 값이 "result" 인 데이터를 출력합니다.
# 3. 위의 결과 중 key 값이 "optionList" 인 데이터를 변수에 저장합니다.
# 4. 3번에서 저장된 값을 반복하며, 원하는 데이터만 추출 및 가공하여 결과 리스트에 저장합니다.

def get_deposit_products():
  api_key = ""

  # 요구사항에 맞도록 이곳의 코드를 수정합니다.
  url = f'https://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
    'auth' : api_key,
    'topFinGrpNo' : '020000',
    'pageNo' : 1
  }
  # json 형태의 반환
  result = requests.get(url,params=params).json()
  # result 에서 optionlist를 가져온다.
  result_key = result.get('result').get('optionList')
  
  result_list = []
  result_value = {}
  

  for x in result_key:
    result_value['금융상품코드'] = x['fin_prdt_cd']
    result_value['저축 금리'] = x['intr_rate']
    result_value['저축 기간'] = x['save_trm']
    result_value['저축금리유형'] = x['intr_rate_type']
    result_value['저축금리유형명'] = x['intr_rate_type_nm']
    result_value['최고 우대금리'] = x['intr_rate2']
    result_list.append(result_value)  # result_value를 리스트 안에 넣어준다.
  

  return result_list

    




# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    # json 형태의 데이터 반환
    result = get_deposit_products()
    # prrint.prrint(): json 을 보기 좋은 형식으로 출력
    pprint.pprint(result)











# numbers = [1,2,3,4,5]
# numbers2 = []
# for num in numbers:
#     numbers2.append(num**2)

# print(numbers2)
