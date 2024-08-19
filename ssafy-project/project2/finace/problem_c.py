import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

csv_path = "archive/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(0, 5))

df_after_2021 = df[df["Date"] >= "2021-01-01"]

# DataFrame 출력
df_after_2021



max_price = df_after_2021['Close'].max()
min_price = df_after_2021['Close'].min()
print('최고 종가 : ', max_price)
print('최저 종가 : ', min_price)