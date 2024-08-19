from django.shortcuts import render, redirect
from .forms import KeywordForm, TrendForm
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64


# Create your views here.

def keyword(request):
    
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


def keyword_detail(request, pk):
    if request.method == 'POST':
        keyword = Keyword.objects.get(pk=pk)
        keyword.delete()
    return redirect('trends:keyword')

def crawling(request):
    trends = Trend.objects.all()
    context = {
        'trends' : trends
    }
    return render(request, 'trends/crawling.html', context)

# 그래프 처리
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


# def crawling_advanced(request):
#     trends = Trend.objects.all()
#     keywords = Keyword.objects.all()
#     results = []

#     for keyword in keywords:
#         url = f'https://www.google.com/search?q={keyword.name}&sca_esv=8e47e8b36fbcdee8&sca_upv=1&source=lnt&tbs=qdr:y'
#         driver = webdriver.Chrome()
#         driver.get(url)
#         html = driver.page_source
#         soup = BeautifulSoup(html, 'html.parser')
#         temp = ''
#         for i in soup.select_one("#result-stats").text:
#             if i.isdecimal():
#                 temp += i
#             if i == '개':
#                 break
#         temp = int(temp)
#         if temp:
#             if keyword.trend_set.exists():
#                 trend = keyword.trend_set.first()
#                 trend.result = temp
#                 trend.search_period = 'year'
#                 trend.save()
#             else:
#                 trend = Trend.objects.create(
#                     keyword=keyword,
#                     result=temp,
#                     search_period='year'
#                 )
#             results.append(temp)
#         else:
#             results.append(0)

#     # 막대 그래프 생성
#     plt.figure(figsize=(10, 6))
#     plt.bar([keyword.name for keyword in keywords], results, label="Trend")
    
#     # 그래프 출력 조정
#     plt.title('Technology Trend Analysis')
#     plt.xlabel('Keyword')
#     plt.ylabel('Result')
#     plt.xticks(rotation=45)
#     plt.grid(True)
#     plt.legend(loc='upper right')

#     # 그래프 이미지를 base64로 변환하여 템플릿으로 전달
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     graph = base64.b64encode(buffer.getvalue()).decode()
#     plt.close()  # 그래프를 닫습니다.

#     context = {
#         'image': f'data:image/png;base64, {graph}',
#     }
#     return render(request, 'trends/crawling_advanced.html', context)
