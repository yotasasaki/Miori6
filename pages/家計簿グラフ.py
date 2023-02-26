import japanize_matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
import openpyxl as px
import streamlit as st


st.set_page_config(layout="wide")

st.title(':blue[家計簿]:sunglasses:')
df=pd.read_excel("./sasaki.xlsx",index_col=0)


fig=plt.figure(figsize=(12,8),facecolor='lightblue')
ax1=fig.add_subplot()
df2=df/2 
df.index=df.index.astype(str)

for i in range(len(df.columns)):
    ax1.bar(df.index,df.iloc[:,i],bottom=df.iloc[:,:i].sum(axis=1) )
    

    for j in range(0,len(df.index)):
        
            s=str(df.columns[i])
            plt.text(j,df.iloc[j,:i].sum()+df2.iloc[j,i],s,ha='center', va='center')


ax1.set(xlabel='月', ylabel='金額')
ax1.set_title("出費棒グラフ",fontsize=20)

plt.show()
st.pyplot(fig)
def color_background_lightgreen(val):
    color = 'lightgreen' if val == "交通費" else '' #1より大なら薄緑、その他は白
    return 'background-color: %s' % color
   
option=st.selectbox("表示したい月",df.index)
if option:
     
    df3=pd.read_excel("./sasaki.xlsx",skiprows=20,sheet_name=option)
    df3["↓↓共用カード払い"]=df3["↓↓共用カード払い"].astype(str)
    df3["↓↓美織払い"]=df3["↓↓美織払い"].astype(str)
    df3["↓↓洋太払い"]=df3["↓↓洋太払い"].astype(str)
    st.dataframe(df3,width=1500)

    



"""
fig=plt.figure(figsize=(12,25),facecolor='lightblue')
ax1=fig.add_subplot(5,2,1)
ax2=fig.add_subplot(5,2,2)
ax3=fig.add_subplot(5,2,3)
ax4=fig.add_subplot(5,2,4)
ax5=fig.add_subplot(5,2,5)
ax6=fig.add_subplot(5,2,6)
ax7=fig.add_subplot(5,2,7)
ax8=fig.add_subplot(5,2,8)
ax9=fig.add_subplot(5,2,9)
ax10=fig.add_subplot(5,2,10)


x=["2022/8","2022/9","2022/10","2022/11","2022/12","2023/1","2023/2","2023/3"]
ax1.plot(x,df["家賃"],label="家賃",color="b",marker="o")
ax2.plot(x,df["電気ガス"],label="電気ガス",color="b",marker="o")
ax3.plot(x,df["水道"],label="水道",color="b",marker="o")
ax4.plot(x,df["駐車場"],label="駐車場",color="b",marker="o")
ax5.plot(x,df["wifi"],label="wifi",color="b",marker="o")
ax6.plot(x,df["交通費"],label="交通費",color="b",marker="o")
ax7.plot(x,df["ガソリン"],label="ガソリン",color="b",marker="o")
ax8.plot(x,df["食費"],label="食費",color="b",marker="o")
ax9.plot(x,df["雑貨"],label="雑貨",color="b",marker="o")
ax10.plot(x,df["その他"],label="その他",color="b",marker="o")


"""