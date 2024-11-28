import streamlit as st
# streamlit run zyouhou.py
st.title('半袖の人')
st.write('これから作品を作っていきます。')
text = st.text_input('あなたの名前を教えてください')
st.write('あなたの名前は、'+text+'です')
condition = st.slider('あなたの今の調子は？',0,100,50)
st.write('コンディション:',condition)
option = st.selectbox('好きな数字を教えてください',list(['1番','2番','3番','4番']))
st.write('あなたが選択したのは、'+option+'です')
import time
st.sidebar.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'lteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')
  from PIL import Image
  img = Image.open('スクリーンショット 2024-11-18 165516.png')
  st.image(img,caption='生活場面',use_column_width=True)
  import pandas as pd
import numpy as np

df = pd.DataFrame(
np.random.rand(100,2)/[50,50] + [35.69,139.70],
columns = ['lat','lon',]#lat lon 緯度と経度
)
#緯度と経度から地図に書き込む
st.map(df)
st.table(df)