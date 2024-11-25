import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 가상 시계열 데이터 생성
time = np.arange(0, 10, 0.1)  # 0부터 10까지 0.1 간격으로 시간 생성
values = np.sin(time)  # 예시로 sin 함수를 사용한 데이터

# pandas DataFrame으로 변환
df = pd.DataFrame({'Time': time, 'Values': values})

# 기울기 구하기 (미분에 해당)
df['Gradient'] = np.gradient(df['Values'])

# 데이터와 기울기 시각화
plt.figure(figsize=(10, 5))
plt.plot(df['Time'], df['Values'], label='Values')
plt.plot(df['Time'], df['Gradient'], label='Gradient')
plt.legend()
plt.show()
