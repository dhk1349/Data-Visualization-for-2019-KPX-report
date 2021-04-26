import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib
path="/home/dhk1349/Desktop/전력시장통계/"
matplotlib.rcParams.update({'font.size': 22})
plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정

AMGO_2019=pd.read_csv(os.path.join(path, "csv_table", "50_2019_통합거래.csv"))
AMGO_2019=AMGO_2019.replace('-', 0)
pie=list(AMGO_2019.iloc[:5, :]["전력거래량AMGO"].astype('int32'))
pie.append(sum(AMGO_2019.iloc[5:18, :]["전력거래량AMGO"].astype('int32')))
pielabel=list(AMGO_2019.iloc[:5, :]["연료원FuelType"])
pielabel.append("Renewable Total")
pielabel=["Nuclear", "Flaming Coal", "Anthracite", "LNG", "Oil", "Renewable Total"]

matplotlib.rcParams.update({'font.size': 25})
plt.rcParams["font.weight"] = "bold"
plt.rcParams['figure.figsize'] = [18, 18]
plt.figure(figsize=(30, 30))
fig1, ax1 = plt.subplots()
ax1.pie(pie, autopct='%1.1f%%')
plt.legend(labels=pielabel, bbox_to_anchor=(1.0, 1.0),fontsize=15,prop={'size': 20})
plt.show()