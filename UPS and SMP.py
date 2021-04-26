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

UPS1=pd.read_csv(os.path.join(path, "csv_table", "108_신재생정산단가.csv"))
UPS2=pd.read_csv(os.path.join(path, "csv_table", "109_신재생정산단가.csv"))
UPS=UPS1.merge(UPS2, how='outer', on='연도Term')
_ysmp=yearly_SMP['가중평균Average'].reset_index()
UPS=pd.concat([UPS,_ysmp], axis=1)

UPS=UPS.set_index("연도Term")
UPS=UPS.drop(columns=["index"])
UPS=UPS.drop(columns=["증감률Change"])
UPS=UPS.replace('-', 0)
UPS=UPS.astype('float32')

UPS=UPS.replace(0, 'NaN')
UPS=UPS.replace('NaN', np.inf)

plt.figure(figsize=(25, 16))
plt.xticks(rotation=45)
matplotlib.rcParams.update({'font.size': 20})
plt.rcParams["font.weight"] = 9
sns.set_style("whitegrid")
ax = sns.lineplot(data=UPS)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
for idx, l in enumerate(ax.lines):
    l.set_linestyle("-")
    # if idx == len(ax.lines)-1:

    #  print("setting line width to 10")
    #  l.set_linewidth(10)
# ax.set_title("SMP and unit price [Won/kWh]")
# ax.legend(["SMP", "Nuclear", "Coal", "LNG", "Renewable"])
# ax.lines[0].set_linewidth(4)
# ax.lines[14].set_linestyle(":")
# ax.lines[14].set_color("black")
ax.lines[14].set_linewidth(5)
labels=["Fuel Cell", "IGCC", "Photovoltaic", "Wind Power", "Off-Gas", "Waste Gas", "Waste", "Hydro", "Ocean", "Bio Gas", "LandFill Gas", "Bio Heavy Oil", "Bio etc.", "Renewable", "SMP"]
plt.legend(labels=labels, bbox_to_anchor=(1.0, 1.0), fontsize=11, loc=2, prop={'size': 11})
plt.show()