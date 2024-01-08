import streamlit as st
import pandas as pd #データ分析
import matplotlib.pyplot as plt

#データ分析関連
df = pd.read_csv("./data/KionData.csv",index_col="月")
# st.dataframe(df)　データを表示
# st.table(df) テーブルにデータを表示
st.line_chart(df) #折れ線グラフ
st.bar_chart(df["2023年"]) #2023のデータを棒グラフで表示

#matplotlib
#2つのオブジェクトを作成
fig,ax = plt.subplots() 
ax.plot(df.index,df["2023年"])
ax.set_title("matplotlib graph")
st.pyplot(fig)