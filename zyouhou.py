import streamlit as st
# streamlit run zyouhou.py
st.title('教えてあげルンです♪')
st.write('このアプリでは、今のあなたにおすすめのメニューを教えルンです🍳')
option1 = st.selectbox('今食べたいものは何ですか？',['','ご飯','パン','麺']) 
if option1 == 'ご飯':
    st.write('あなたは今、ご飯が食べたいんですね！')
elif option1 == 'パン':
    st.write("あなたは今、パンが食べたいんですね！")
elif option1 == '麺':
    st.write('あなたは今、麺が食べたいんですね！')
option2 = st.selectbox('何風がいいですか？',(['','和風','洋風','中華','イタリアン']))
if option2 == '和風':
    st.write('あなたは今、和風の気分なんですね！')
elif option2 == '洋風':
    st.write('あなたは今、洋風の気分なんですね！')
elif option2 == '中華':
    st.write('あなたは今、中華の気分なんですね！')
elif option2 == 'イタリアン':
    st.write('あなたは今、イタリアンの気分なんですね！')        
option3 = st.selectbox('どんな感じ？',(['','あっさり','がっつり']))
if option3 == 'あっさり':
    st.write('あっさりしたいんですね！')
elif option3 == 'がっつり':
    st.write('がっつりしたいんですね！')

if option1 == 'ご飯':
    if option2 == '和風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはお茶漬けです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E3%81%8A%E8%8C%B6%E6%BC%AC%E3%81%91")
if option1 == 'ご飯':
    if option2 == '洋風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはオムライスです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/18519604-%E5%8B%95%E7%94%BB%E3%81%82%E3%82%8A%E7%B0%A1%E5%8D%98%E3%81%B5%E3%82%8F%E3%81%A8%E3%82%8D%E3%82%AA%E3%83%A0%E3%83%A9%E3%82%A4%E3%82%B9")
if option1 == 'ご飯':
    if option2 == '中華':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューは海老チャーハンです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/17830192-%E3%81%B5%E3%82%93%E3%82%8F%E3%82%8A%E7%82%92%E3%82%8A%E5%8D%B5%E3%81%AE%E6%B5%B7%E8%80%81%E3%83%81%E3%83%A3%E3%83%BC%E3%83%8F%E3%83%B3")
if option1 == 'ご飯':
    if option2 == 'イタリアン':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはシーフードサラダライスです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/18072615-%E3%82%B7%E3%83%BC%E3%83%95%E3%83%BC%E3%83%89%E3%82%A2%E3%83%9C%E3%82%AB%E3%83%89%E3%81%AE%E3%83%A9%E3%82%A4%E3%82%B9%E3%82%B5%E3%83%A9%E3%83%80")
if option1 == 'ご飯':
    if option2 == '和風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはかつ丼です！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/19573712-%E4%BA%BA%E5%89%8D%E3%81%8A%E3%81%84%E3%81%97%E3%82%AB%E3%83%84%E4%B8%BC%E3%82%BF%E3%83%AC%E4%BD%9C%E3%82%8A%E6%96%B9")
if option1 == 'ご飯':
    if option2 == '洋風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはガーリックステーキライスです！')
            st.link_button("Go to gallery", "https://oceans-nadia.com/user/253470/recipe/437792")
if option1 == 'ご飯':
    if option2 == '中華':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはチャーハンです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/19936975-%E8%B6%85%E7%B0%A1%E5%8D%98%E5%A4%B1%E6%95%97%E3%81%AA%E3%81%97%E5%9F%BA%E6%9C%AC%E3%81%AE%E3%83%91%E3%83%A9%E3%83%91%E3%83%A9%E7%82%92%E9%A3%AF")
if option1 == 'ご飯':
    if option2 == 'イタリアン':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはラザニアです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/19405757-%E3%83%A9%E3%82%B6%E3%83%8B%E3%82%A2")
if option1 == 'パン':
    if option2 == '和風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューは和風サンドイッチです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E5%92%8C%E9%A2%A8%20%E3%82%B5%E3%83%B3%E3%83%89%E3%82%A4%E3%83%83%E3%83%81")
if option1 == 'パン':
    if option2 == '洋風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューは洋風サンドイッチです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E5%8E%9A%E5%88%87%E3%82%8A%20%E3%82%B5%E3%83%B3%E3%83%89%E3%82%A4%E3%83%83%E3%83%81")
if option1 == 'パン':
    if option2 == '中華':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューは中華風サンドイッチです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E4%B8%AD%E8%8F%AF%E3%82%B5%E3%83%B3%E3%83%89")
if option1 == 'パン':
    if option2 == 'イタリアン':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはブルスケッタです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E3%83%96%E3%83%AB%E3%82%B9%E3%82%B1%E3%83%83%E3%82%BF%20%E6%9C%AC%E6%A0%BC")
if option1 == 'パン':
    if option2 == '和風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはカツサンドです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E3%82%AB%E3%83%84%E3%82%B5%E3%83%B3%E3%83%89%20%E7%B0%A1%E5%8D%98")
if option1 == 'パン':
    if option2 == '洋風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはフィリーチーズステーキサンドです！')
            st.link_button("Go to gallery", "https://delishkitchen.tv/recipes/371422010154157202")
if option1 == 'パン':
    if option2 == '中華':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューは肉まんです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E8%82%89%E3%81%BE%E3%82%93%20%E7%B0%A1%E5%8D%98")
if option1 == 'パン':
    if option2 == 'イタリアン':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはミートボールサブです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/17678615-%E5%A4%A9%E4%B8%8B%E7%84%A1%E6%95%B5%E3%83%9F%E3%83%BC%E3%83%88%E3%83%9C%E3%83%BC%E3%83%AB%E3%82%B5%E3%83%96")
if option1 == '麺':
    if option2 == '和風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはそうめんです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E3%81%9D%E3%81%86%E3%82%81%E3%82%93")
if option1 == '麺':
    if option2 == '洋風':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはペペロンチーノです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/20295838-%E8%B6%85%E7%B0%A1%E5%8D%98%E6%9C%AC%E6%A0%BC%E3%83%9A%E3%83%9A%E3%83%AD%E3%83%B3%E3%83%81%E3%83%BC%E3%83%8E")
if option1 == '麺':
    if option2 == '中華':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューは冷やし中華です！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/17362568-%E5%A4%A7%E5%A5%BD%E8%A9%95%E3%81%AE%E5%86%B7%E3%82%84%E3%81%97%E4%B8%AD%E8%8F%AF")
if option1 == '麺':
    if option2 == 'イタリアン':
        if option3 == 'あっさり':
            st.write('あなたにおすすめのメニューはレモンバジルパスタです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/17716812-%E7%88%BD%E3%82%84%E3%81%8B%E3%83%90%E3%82%B8%E3%83%AB%E3%83%AC%E3%83%A2%E3%83%B3%E3%81%AE%E3%83%91%E3%82%B9%E3%82%BF")
if option1 == '麺':
    if option2 == '和風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューは鍋焼きうどんです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/search/%E9%8D%8B%E7%84%BC%E3%81%8D%E3%81%86%E3%81%A9%E3%82%93")
if option1 == '麺':
    if option2 == '洋風':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはカルボナーラです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/18951127-%E7%B0%A1%E5%8D%98%E7%89%9B%E4%B9%B3%E3%81%A8%E5%85%A8%E5%8D%B5%E6%BF%83%E5%8E%9A%E3%82%AB%E3%83%AB%E3%83%9C%E3%83%8A%E3%83%BC%E3%83%A9")
if option1 == '麺':
    if option2 == '中華':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはラーメンです！')
            st.link_button("Go to gallery", "http://www.konshinya.com/shop/higashiwada.html")
if option1 == '麺':
    if option2 == 'イタリアン':
        if option3 == 'がっつり':
            st.write('あなたにおすすめのメニューはペスカトーレです！')
            st.link_button("Go to gallery", "https://cookpad.com/jp/recipes/17442456-%E3%83%9A%E3%82%B9%E3%82%AB%E3%83%88%E3%83%BC%E3%83%AC")
sentiment_mapping = ["one", "two", "three", "four", "five"]
st.write('おすすめしたメニューは満足できましたか？')
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")





















