import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_path = "archive/NFLX.csv"

# CSV 파일 읽어오기 (첫 번째, 마지막 열 제외)
df = pd.read_csv(csv_path, usecols=range(0, 5))

# DataFrame 출력
df

