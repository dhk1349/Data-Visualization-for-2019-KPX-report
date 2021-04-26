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

SMP_2019=pd.read_csv(os.path.join(path, "csv_table", "48_2019SMP.csv"))
Trading_2019=pd.read_csv(os.path.join(path, "csv_table", "48_거래량_거래금액.csv"))

col=list(SMP_2019.columns)[1:]
col.append("_")
SMP_2019.columns=col
SMP_2019=SMP_2019.drop(columns=["_"])
col=list(Trading_2019.columns)[1:]
col.append("_")
Trading_2019.columns=col
Trading_2019=Trading_2019.drop(columns=["_"])
Trading_2019.columns=[i for i in range(1,14)]

plt.rc('font', family='NanumGothicCoding')
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")
ax=sns.lineplot(data=Trading_2019.iloc[:, :-1].T)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
plt.savefig("Trading volume and Payment of Settlement.png")


AMGO_list=glob(path+"csv_table/*거래.csv")
AMGO_list=sorted(AMGO_list)
month_dict={}
for m in AMGO_list:
  # print(m.split("/")[-1][8:10])
  month_dict[m.split("/")[-1][8:10]]=pd.read_csv(m)
  month_dict[m.split("/")[-1][8:10]]=month_dict[m.split("/")[-1][8:10]].drop([7, 14, 17 ])

AMGO_concat= pd.DataFrame()
for pd_key in month_dict.keys():
  if pd_key!="통합":
    AMGO_concat=pd.concat([AMGO_concat, month_dict[pd_key]["전력거래량AMGO"]], axis=1)

AMGO_concat.columns=[i for i in range(1, 13)]
AMGO_concat=AMGO_concat.reset_index()
AMGO_concat=AMGO_concat.drop(columns=["index"])
AMGO_concat['Type']=list(month_dict["1_"]["연료원FuelType"])
AMGO_concat=AMGO_concat.set_index('Type')
T_AMGO=AMGO_concat.T.squeeze()
T_AMGO=T_AMGO.astype('int32')
plt.figure(figsize=(18, 12))
sns.set_style("whitegrid")
ax=sns.lineplot(data=T_AMGO.iloc[:, :-1])
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
for idx, l in enumerate(ax.lines):
  l.set_linestyle("-")
  #if idx == 4:
  #  l.set_linestyle(":")
label = ["Nuclear", "Flaming Coal", "Anthracite", "LNG", "Oil", "Pumped Storage", "Fuel Cell", "Photovoltaic", "Wind Power", "Hydro", "Ocean", "Bio gas", "LandFill Gas", "Bio etc.","Off-Gas", "Waste", "Others", "Total"]
plt.legend(labels=label[:-1], bbox_to_anchor=(1.0, 1.0),fontsize=11, loc=2, prop={'size': 11})
#ax.set_title("SMP and unit price [Won/kWh]")
#ax.legend(["SMP", "Nuclear", "Coal", "LNG", "Renewable"])
#ax.lines[0].set_linewidth(4)
#ax.lines[4].set_linewidth(4)
plt.show()

plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")
ax=sns.lineplot(data=T_AMGO)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
for idx, l in enumerate(ax.lines):
  l.set_linestyle("-")
  if idx == len(ax.lines)-1: #18th
    l.set_linestyle(":")
    l.set_linewidth(10)

#ax.set_title("SMP and unit price [Won/kWh]")
#ax.legend(["SMP", "Nuclear", "Coal", "LNG", "Renewable"])
#ax.lines[0].set_linewidth(4)
ax.lines[17].set_linewidth(5)
plt.legend(labels=label, bbox_to_anchor=(1.0, 1.0),fontsize=11, loc=2, prop={'size': 11})
plt.show()

newdf=T_AMGO[list(AMGO_concat.index)[5:-1]]
plt.figure(figsize=(16, 10))
sns.set_style("whitegrid")
ax=sns.lineplot(data=newdf)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
for idx, l in enumerate(ax.lines):
  l.set_linestyle("-")
  #if idx == 4:
  #  l.set_linestyle(":")
#ax.set_title("SMP and unit price [Won/kWh]")
#ax.legend(["SMP", "Nuclear", "Coal", "LNG", "Renewable"])
#ax.lines[0].set_linewidth(4)
#ax.lines[4].set_linewidth(4)
label = ["Pumped Storage", "Fuel Cell", "Photovoltaic", "Wind Power", "Hydro", "Ocean", "Bio gas", "LandFill Gas", "Bio etc.","Off-Gas", "Waste", "Others"]
plt.legend(labels=label, bbox_to_anchor=(1.0, 1.0),fontsize=11, loc=2, prop={'size': 11})

plt.show()