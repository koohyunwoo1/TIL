'''
다음은 이형기 시인의 "낙화"의 한 구절이다.
- 1연
	가야할 때 언제인가를
	분명히 알고 가는 이의
	뒷모습은 얼마나 아름다운가.

나는 이 시를 보며 '나는 내가 가야할 때가 언제일까?' 를 생각해 보았다.
'''
import copy

# 기존 catalog 변수
catalog = {
    "poet": "이형기",
    "title": "낙화",
    "lines": [
        "가야할 때 언제인가를",
        "분명히 알고 가는 이의",
        "뒷모습은 얼마나 아름다운가."
    ]
}

# catalog 변수를 이용하여 새로운 변수에 값을 할당 (깊은 복사)
catalog_backup = copy.deepcopy(catalog)

# catalog 변수의 잘못 저장된 값을 수정
# "가야할 때 언제인가를" -> "가야 할 때 언제일까를" 로 수정
catalog["lines"][0] = "가야 할 때 언제일까를"

# 백업 정보와 원본 비교
print(catalog_backup is catalog)
