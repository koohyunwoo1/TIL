import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "archive/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(0, 5))

df_after_2021 = df[df["Date"] >= "2021-01-01"]

df_after_2021["Date"] = pd.to_datetime(df_after_2021["Date"])

# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_after_2021['Date'], df_after_2021['Close'])


# 그래프 제목 설정
plt.title('Close Prices over Time')

# x축 레이블 설정
plt.xlabel('Date')

# y축 레이블 설정
plt.ylabel('Close')

# 그래프 표시
plt.show()