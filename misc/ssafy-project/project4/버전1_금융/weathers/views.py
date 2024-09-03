from django.shortcuts import render
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import numpy as np
import re
# Create your views here.

# plt.rcParams['font.family'] = 'Malgun Gothic'
# plt.rcParams['axes.unicode_minus'] = False

def problem1(request):
    df = pd.read_csv('austin_weather.csv')
    df = df.to_html()
    context = {
        'df': df
    }
    return render(request, 'weathers/problem1.html', context)


def problem2(request):
    df = pd.read_csv('austin_weather.csv')

    df['Date'] = pd.to_datetime(df['Date'])
    # df_sampled = df.resample('1Y').mean()
    # print(df_sampled)


    plt.plot(df['Date'] , df['TempHighF'] , label = 'High Temperature')
    plt.plot(df['Date'] , df['TempAvgF'], label = 'Average Temperature')
    plt.plot(df['Date'] , df['TempLowF'], label = 'Low Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend(loc='lower center')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'graph_data' : graph_data
    }
    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df = pd.read_csv('austin_weather.csv')
    
    df['Date'] = pd.to_datetime(df['Date'])

    

    # df['Date'].to_frame()
    # print(type(df['Date']))


    # df_sampled = df['TempHighF'].resample('1Y').mean()
    # print(df_sampled)

    # df = df.resample('M', on='Date').mean()
    # print(df)


    df_temp = df[['Date', 'TempHighF', 'TempAvgF', 'TempLowF']]

    df_monthly_avg = df_temp.resample('M', on='Date').mean()


    plt.plot(df_monthly_avg.index , df_monthly_avg['TempHighF'] , label = 'High Temperature')
    plt.plot(df_monthly_avg.index , df_monthly_avg['TempAvgF'], label = 'Average Temperature')
    plt.plot(df_monthly_avg.index , df_monthly_avg['TempLowF'], label = 'Low Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend(loc='lower center')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'graph_data' : graph_data
    }
    return render(request, 'weathers/problem3.html', context)



def problem4(request):
    df = pd.read_csv('austin_weather.csv')


    x = np.arange(5)
    weathers = ['No Events', 'Rain', 'Thunderstorm', 'Fog', 'Snow']


    times = [0] * 5 

    # print(list(re.split(r'[,\s]+', df['Events'][0])))
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

    plt.bar(x, times)
    plt.xticks(x, weathers)
    plt.title('Events Counts')
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.grid(True)

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    
    buffer.seek(0)

    graph_data = base64.b64encode(buffer.getvalue()).decode()

    context = {
        'graph_data' : graph_data,
    }
    return render(request, 'weathers/problem4.html', context)