## 데이터 사이언스 프로세스

- 필요한 정보를 추출하는 5가지 단계
  1. 문제정의 : 해결하고자 하는 문제 정의
  2. 데이터 수집 : 문제 해결에 필요한 데이터 수집
    - API
    - 캐글(csv)
  3. 데이터 전처리(정제) : 실질적인 분석을 수행하기 위해 데이터를 가공하는 단계
  4. 데이터 분석 : 전처리가 완료된 데이터에서 필요한 정보를 추출하는 단계
  5. 결과 해석 및 공유 : 의사 결정에 활용하기 위해 결과를 해석하고 시각화 


### Django 에서 데이터 사이언스 패키지를 사용하는 이유 ?
-  결과를 웹 페이지에서 보여주기 위함

# Problem 1
```python
# views.py
df = pd.read_csv('austin_weather.csv')
df = df.to_html()
```

- df = df.to_html()가 없으면 엑셀형태가 그대로 출력된다. html에서 제대로 된 테이블 형태불러오기 위해서 아래와 같은 html형식으로 변환시켜야 한다.

```html

  <tr>
  <th>1318</th>
      <td>2017-07-31</td>
      <td>99</td>
      <td>88</td>
      <td>77</td>
      <td>66</td>
      <td>61</td>
      <td>54</td>
      <td>64</td>
      <td>43</td>
      <td>22</td>
      <td>30.04</td>
      <td>29.97</td>
      <td>29.91</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>12</td>
      <td>4</td>
      <td>20</td>
      <td>0</td>
      <td></td>
    </tr>
  </tbody>
</table>

```

```html
<!-- problem1.html -->
{% extends "base.html" %}

{% block content %}
<h1>문제1. 데이터 읽어오기</h1>
{{ df|safe }}

{% endblock content %}

```
- df|safe가 무엇인지 ?
  - {{ df|safe }}는 DataFrame인 df를 HTML로 렌더링할 때, DataFrame이 가진 HTML 태그를 그대로 출력하도록 지시하는 필터이다.



---

# Problem 2

```py

# views.py

plt.plot(df['Date'] , df['TempHighF'] , label = 'High Temperature')
plt.plot(df['Date'] , df['TempAvgF'], label = 'Average Temperature')
plt.plot(df['Date'] , df['TempLowF'], label = 'Low Temperature')

plt.legend(loc='lower center')
```

- 그래프가 2개이상일 때 , 라벨 없이 legend함수를 호출했을때 그래프에 표시되지 않았다.
- 위치를 수정하기 위해서는 loc값을 아래와 같이 지정해줄수있다

```

Location String   Location Code
===============   =============
'best'            0
'upper right'     1
'upper left'      2
'lower left'      3
'lower right'     4
'right'           5
'center left'     6
'center right'    7
'lower center'    8
'upper center'    9
'center'          10
===============   =============


```

---
# Problem 3

```py

# views.py

# 오류 코드
df['Date'].to_frame()
print(type(df['Date']))

df_sampled = df['TempHighF'].resample('1Y').mean()
print(df_sampled)
df = df.resample('M', on='Date').mean()
print(df)

# 오류 : Only valid with DatetimeIndex, TimedeltaIndex or PeriodIndex, but got an instance of 'RangeIndex'


# 정답 코드
df_temp = df[['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]

df_monthly_avg = df_temp.resample('M', on='Date').mean()

```


- 오류 코드를 실행 했을 시 다른 컬럼에 숫자가 아닌 다른 값들이 존재해 평균값을 낼 수 없었고 위와 같은 오류가 발생했다.

- 평균 값이 필요한 데이터 들을 원본의 데이터에서 전처리 해주어 새로운 변수에 할당해주었고, 그 뒤에 평균을 구해주어 오류를 해결했다.

- groupby 대신 resample사용하기 위해서 resample 하기전에 데이터를 전처리 해준뒤 해준다.
- 다른 조는 groupby로 해결하는것을 보아 다음에는 groupby를 통해 해결해보자.

---
# Problem 4


```py

# views.py

import re


for event in df['Events']:
      weather = list(re.split(r'[,\s]+', event))
      for w in weather:
          if w == 'Rain':
              times[1] += 1
          elif w == 'Thunderstorm':
              times[2] += 1
          elif w == 'Fog':
              times[3] += 1
          elif w == 'Snow':
              times[4] += 1
          # \s를 split했을때 2개의 ''가 생긴다.
          # 그렇기 때문에 0.5씩 더해준다.
          else:
              print(weather)
              times[0] += 0.5

```

- 기존의 데이터에서 막대 그래프를 만들기 위해 새로운 데이터를 만들어주었다.
- csv파일에서 '\s' 값을 **re.split(r'[,\s]+'** 로 나누어 주면 하나의 빈 값이 나올 것으로 예상했지만, 2개의 '' 값이 리스트에 담겨져있었다. else 문을 실행했을 때 값이 2개가 나와 0.5를 더해주는 방법을 채택하였다. 다른 방법으로는 빈 문자열일때 한 번 더한뒤 for문을 break시키는 방법이 있을 것 같다.