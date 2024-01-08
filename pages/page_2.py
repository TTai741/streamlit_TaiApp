import streamlit as st
import datetime #日付をとるために

with st.form(key="profile_form"): #これがあることでボタンが押されないと画面がリロードされない

        #テキストボックス
        name = st.text_input("名前")
        address = st.text_input("住所")
        
        #セレクトボックス
        age_category = st.selectbox("年齢層",("子供(18歳未満)","大人(18歳以上)"))

        #ラジオボタン
        age_categoryB = st.radio("性別",("男性","女性"))
        
        #複数選択
        hobby = st.multiselect("趣味",("スポーツ","読書","プログラミング","アニメ・映画","釣り","料理"))

        #チェックボックス
        mail_subscribe = st.checkbox("メールマガジンを購読する")
        
        #スライダー
        height = st.slider("身長",min_value=110,max_value=220)
        
        #日付
        start_date = st.date_input("開始日",datetime.date(2024,1,1))
        
        #カラーピッカー   ＃00f900はデフォルト
        color = st.color_picker("テーマカラー","#00f900")
        
        #ボタン
        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
        
        
        if submit_btn:
            st.text(f"ようこそ！{name}さん！{address}に書籍を送りました！")
            st.text(f"年齢層:{age_category}")
            st.text(f"性別:{age_categoryB}")
            st.text(f"趣味:{', '.join(hobby)}")
            if mail_subscribe:
                st.text("メールマガジン:購読する")
            else:
                st.text("メールマガジン:購読しない")
            st.text(f"身長:{height}cm")
            st.text(f"開始日:{start_date}")