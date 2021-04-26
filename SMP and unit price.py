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

yearly_SMP=pd.read_csv(os.path.join(path, "csv_table", "40_연간 SMP.csv"))
col=list(yearly_SMP.columns[1:])
col.append("-")
yearly_SMP.columns=col
yearly_SMP=yearly_SMP.drop(columns=["-"])

plt.figure(figsize=(16, 16))
plt.xticks(rotation=45)
sns.set_style("whitegrid")
ax=sns.lineplot(data=yearly_SMP["가중평균Average"])
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
plt.show()
plt.savefig("SMP.png")
print("Saving SMP")



unit_price=pd.read_csv(os.path.join(path, "csv_table", "39_연료별정상단가.csv"))
unit_col=list(unit_price.columns)
for idx, i in enumerate(unit_col):
  if i=="연도Term":
    unit_col[idx]='Year'
unit_price.columns=unit_col
unit_price=unit_price.set_index('Year')
# unit_price=unit_price.astype('int32')
labels=["Nuclear", "Coal", "LNG", "Oil", "Pumped-Storage", "Renewable"]
plt.figure(figsize=(16, 16))
plt.xticks(rotation=45)
sns.set_style("whitegrid")
ax=sns.lineplot(data=unit_price.iloc[:, :6])
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
leg=ax.legend(labels=labels, fontsize=15, prop={'size': 15})
for idx, l in enumerate(ax.lines):
  l.set_linestyle("-")
  if idx<6:
    print(leg.get_lines())
    print(idx)
    leg.get_lines()[idx].set_linestyle("-")

plt.show()
plt.savefig("unit_price.png")
print("Saving unit price")


integrated_year_price=pd.concat([yearly_SMP["가중평균Average"], unit_price.iloc[:, :3], unit_price.iloc[:, 5:6]], axis=1)
plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")
plt.xticks(rotation=45)
ax=sns.lineplot(data=integrated_year_price)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
for idx, l in enumerate(ax.lines):
  l.set_linestyle("-")
  if idx == 4:
    l.set_linestyle(":")
ax.set_title("SMP and unit price [Won/kWh]")
ax.legend(["SMP", "Nuclear", "Coal", "LNG", "Renewable"])
ax.lines[0].set_linewidth(4)
ax.lines[4].set_linewidth(4)
plt.show()
plt.savefig("SMP and unit price.png")
print("Saving SMP and unit price[Wopn/kWh]")

