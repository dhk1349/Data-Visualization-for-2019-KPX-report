import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from glob import glob
import pandas as pd
import matplotlib.ticker as ticker
import matplotlib
import matplotlib.font_manager
import geopandas as gpd

print([f.name for f in matplotlib.font_manager.fontManager.ttflist if 'Nanum' in f.name])
matplotlib.rcParams.update({'font.size': 22})
plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus=False) # 마이너스 폰트 설정

shapefile=os.path.join("gadm36_KOR_shp", "gadm36_KOR_1.shp")
gdf=gpd.read_file(shapefile)[["NAME_1", 'geometry']]
gdf.columns = ['name', 'geometry']

files=glob("./csv_table/*신재생거래량.csv")
files=sorted(files)
renewdict={}
for f in files:
    renewdict[f.split('/')[-1][:11]]=pd.read_csv(f)

lst=list(renewdict.keys())
for idx, df_key in enumerate(lst):
    if idx%2==0:
        df1=renewdict[df_key]
    elif idx%2==1:
        renewdict[str(int((idx+1)/2))]=renewdict[df_key].merge(df1, how='outer', on='구분Type')
        renewdict[str(int((idx+1)/2))]=renewdict[str(int((idx+1)/2))].set_index("구분Type")
        # print(str(int((idx+1)/2)))


newcol=['Seoul', 'Incheon', 'Daejeon', 'Gwangju', 'Daegu', 'Sejong', 'Ulsan', 'Busan', 'Gyeonggi-do', 'Gangwon-do', 'Gyeongsangnam-do', 'Gyeongsangbuk-do', 'Jeollanam-do', 'Jeollabuk-do', 'Chungcheongnam-do', 'Chungcheongbuk-do', 'Jeju'] #Total will be erased
for i in range(1, 13):
    renewdict[str(i)]=renewdict[str(i)].drop(columns=['전국Total'])
    renewdict[str(i)].columns=newcol
    renewdict[str(i)]=renewdict[str(i)].replace('-', 0)
    # print(renewdict[str(i)].columns)
"""
for i in range(1,13):
    data={'data'+str(i):list(renewdict[str(i)].iloc[3:4, :].T['풍력']), 'name':['Seoul', 'Incheon', 'Daejeon', 'Gwangju', 'Daegu', 'Sejong', 'Ulsan',
       'Busan', 'Gyeonggi-do', 'Gangwon-do', 'Gyeongsangnam-do',
       'Gyeongsangbuk-do', 'Jeollanam-do', 'Jeollabuk-do', 'Chungcheongnam-do',
       'Chungcheongbuk-do', 'Jeju']}
    df=pd.DataFrame(data)
    gdf=gdf.merge(df, on='name', how='outer')
"""
for i in range(1,13):
    data={'data'+str(i):list(renewdict[str(i)].iloc[2:3, :].T['태양광']), 'name':['Seoul', 'Incheon', 'Daejeon', 'Gwangju', 'Daegu', 'Sejong', 'Ulsan',
       'Busan', 'Gyeonggi-do', 'Gangwon-do', 'Gyeongsangnam-do',
       'Gyeongsangbuk-do', 'Jeollanam-do', 'Jeollabuk-do', 'Chungcheongnam-do',
       'Chungcheongbuk-do', 'Jeju']}
    df=pd.DataFrame(data)
    gdf=gdf.merge(df, on='name', how='outer')

fig, axes = plt.subplots(2, 6, figsize=(60, 30),sharex=True, sharey=True, )
# plt.legend(bbox_to_anchor=(1.0, 1.0),fontsize=15, loc=2, prop={'size': 10})

for idx, ax in enumerate(axes.flat):
    gdf.plot(ax=ax, column='data'+str(idx+1), legend=True, legend_kwds={'loc':'center right', 'fontsize':10,'bbox_to_anchor': (1.3, 1.0), 'prop':{'size':15}}, cmap="OrRd", scheme="quantiles")
    ax.set_title(str(idx+1))
    ax.axis('off')
    # ax.axis('off')
plt.savefig("Solar.jpg")
