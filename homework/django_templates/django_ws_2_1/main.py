import requests
import pprint

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbvision9811111558001'
params = {
    'ttbkey': API_KEY,
    'QueryType' : 'ItemNewSpecial',
    'start' : 1,
    'MaxResult' : 50,
    'SearchTarget' : 'Book',
    'Output' : 'JS',
    'Version' : 20131101
}
result = []
response = requests.get(API_URL, params=params)
book_lst = response.json()
for item in book_lst['item']:
    book_info = {
                '제목': item['title'],
                '저자': item['author'],
                '출간일': item['pubDate'],
                '국제 표준 도서 번호': item['isbn']
    }
    result.append(book_info)
pprint.pprint(result)
