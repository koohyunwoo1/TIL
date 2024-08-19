import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "archive/NFLX.csv"

df = pd.read_csv(csv_path)
df_after_2021 = df[df["Date"] >= "2021-01-01"]

df_after_2021["Date"] = pd.to_datetime(df_after_2021["Date"],)
df_after_2021.dtypes
# 월 별로 만들어보기

df_Month = df_after_2021.groupby(by = df_after_2021["Date"].dt.month).mean()


# 그래프 그리기 (가로, 세로 축에 표시될 데이터를 차례로 기입)
plt.plot(df_Month['Date'], df_Month['Close'])


# # 그래프 제목 설정
plt.title('Montyly Average Close Price')

# # x축 레이블 설정
plt.xlabel('Date')

# # y축 레이블 설정
plt.ylabel('Average Close Price')

# # 그래프 표시
plt.show()