import streamlit as st
from PIL import Image #画像用

#テキスト関連
st.title("Taiアプリ")
st.caption("アプリ実行テスト中")

#画像
Image_AK = Image.open("./data/AKsuit.jpg")
st.image(Image_AK,width=200)

#動画
st.video("https://youtu.be/rrv4s5EQy7E?feature=shared")