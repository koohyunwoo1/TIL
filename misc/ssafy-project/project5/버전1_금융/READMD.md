### 데이터 수집
- 데이터 수집은 다양한 기술과 방법을 활용 가능
  - 웹 스크래핑 : 웹 페이지에서 데이터를 추출하는 기술
  - 웹 크롤링 : 웹 페이지를 자동으로 탐색하고 데이터를 수집하는 기술
  - Open API 활용 : 공개된 API를 통해 데이터를 수집
  - 데이터 공유 플랫폼 활용 : 다양한 사용자가 데이터를 공유하고 활용할 수 있는 온라인 플랫폼
    - 종류 : 캐글, Data world, 데이콘, 공공데이터포털


#### 웹 크롤링 ?
- 여러 웹 페이지를 돌아다니며 원하는 정보를 모으는 기술
- 즉, 웹 사이트를 돌아다니며 필요한 데이터를 추출하여 활용할 수 있도록 자동화된 프로세스

#### 웹 크롤링 프로세스
- 웹 페이지 다운로드
  - 해당 웹 페이지의 HTML, CSS , JavaScript 등의 코드를 가져오는 단계
- 페이지 파싱
  - 다운로드 받은 코드를 분석하고 필요한 데이터를 추출하는 단계
- 링크 추출 및 다른 페이지 탐색
  - 다른 링크를 추출하고, 다음 단계로 이동하여 원하는 데이터를 추출하는 단계
- 데이터 추출 및 저장
  - 분석 및 시각화에 사용하기 위해 데이터를 처리하고 저장하는 단계


#### 참고
![Alt text](image.png)

# problem B.
```py
def keyword_detail(request, pk):
    if request.method == 'POST':
        keyword = Keyword.objects.get(pk=pk)
        keyword.delete()
    return redirect('trends:keyword')

```
- delete를 할려면 pk를 알아야 하는데 pk를 받아오는 것이 기억이 안나 공식문서를 읽어보아서 해결하였음.
- https://docs.djangoproject.com/en/4.2/ref/forms/

# problem C.
```py

 keywords = Keyword.objects.all()
    if request.method == "POST":
        url = f'https://www.google.com/search?q={request.POST["name"]}'
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')

        
        form = KeywordForm(request.POST)


        if form.is_valid():
            keyword = form.save()
            # print(soup.select_one("#result-stats").text)
            temp = ''
            for i in soup.select_one("#result-stats").text:
                if i.isdecimal():
                    temp += i
                if i == '개':
                    break
            temp = int(temp)
            trend = Trend()
            print(trend.id)
            trend.name = request.POST['name']
            trend.result = temp
            # trend.result = soup.select_one("#result-stats")
            trend.search_period = 'all'
            print(trend.search_period)
            trend.keyword = keyword
            trend.save()

    else:
        form = KeywordForm()
    context = {
        'form' : form,
        'keywords' : keywords,
    }
    return render(request, 'trends/keyword.html', context)


```

- 문제점 : 
- 1. 키워드를 추가 할 때, 크롤링한 trend를 같이 추가해서 중복제거가 힘들어지고 , search_period 별로 데이터 분류가 힘들었다.
- 2. 이로 인해 중복된 데이터가 계속 생성되었다.
# problem D & E
```py


def export_pic():
    # BytesIO 객체를 생성하고, buffer라는 변수에 할당
    buffer = BytesIO()
    # buffer에 그래프를 png 형태로 저장
    plt.savefig(buffer, format='png')
    # buffer의 내용을 인코딩
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    return img_base64



def crawling_histogram(request):
    trends = Trend.objects.all()
    name = [trend.name for trend in trends]
    result = [trend.result for trend in trends]
    
    # 히스토그램에 데이터 입력
    plt.figure(figsize=(10, 6))
    plt.bar(name, result, label="Trend")

    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(loc='upper right')

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, 'trends/crawling_histogram.html', context)

def crawling_advanced(request):
    trends = Trend.objects.all()
    names = [trend.name for trend in trends]
    results = []
    
    for name in names:
        url = f'https://www.google.com/search?q={name}&tbs=qdr:y'
        driver = webdriver.Chrome()
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        temp = ''
        for i in soup.select_one("#result-stats").text:
            if i.isdecimal():
                temp += i
            if i == '개':
                break
        temp = int(temp)
        trend = Trend()
        # print(trend.id)
        trend.result = temp
        # trend.result = soup.select_one("#result-stats")
        trend.search_period = 'year'
        for keyword in Keyword.objects.all():
            if keyword.name == name:
                trend.keyword = keyword
                break
        trend.save()
        
    plt.figure(figsize=(10, 6))
    plt.bar(names, results, label="Trend")
    
    # 그래프 출력 조정
    plt.title('Technology Trend Analysis')
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend(loc='upper right')

    context = {
        'image': f'data:image/png;base64, {export_pic()}',
    }
    return render(request, 'trends/crawling_advanced.html', context)

```

- 문제점 :
- B에서의 문제점이 D와 E까지 이어졌다.
- 히스토그램을 생성하는데 중복이 제거가 되지 않아 똑같은 키워드의 값들이 여러개의 히스토그램에 출력되었다.
- 데이터를 여러번 삭제해보았지만 설계가 잘못되어서 처음부터 다시 해야될거같다.