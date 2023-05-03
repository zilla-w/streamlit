import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [40, 30 ,20 ,10]
})
    
st.write(df)

#dataframeは引数として縦と横のサイズを指定できる
st.dataframe(df, width=100, height=100)

#highlight_max()で最大値に色付けできる　axis=0は列、axis=1は行
st.dataframe(df.style.highlight_max(axis=1))

#dataframe() 「動的」なテーブルを使う、ソートができる
#table()　「静的」(static)なテーブルを使う、テーブルを表示させるだけ
st.table(df)

#マジックコマンド
# #で見出しを表示、#の数で大きさを変えられる
# ```python pythonコードを表記
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

ch = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(ch)
st.bar_chart(ch)

mp = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(mp)

st.write('Display Image')

img = Image.open('godzilla1.jpg')
st.image(img, caption='Godzilla', use_column_width=True)

# チェックボックスによる表示可否
# チェックを入れる = True、　チェックを外す = False
if st.checkbox('Show Image'):
    img = Image.open('godzilla2.jpg')
    st.image(img, caption='Godzilla vs Gong', use_column_width=True)

# セレクトボックスによる動的変更
select_math = st.selectbox(
    'あなたの好きな数字を教えてください。',
    list(range(1, 11))
)
st.write('あなたの好きな数字は',select_math, 'ですね' )

# テキスト入力
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は：', text

# スライダー
#slider('表示文章',最小値 ,最大値 ,デフォルト値)
condition = st.slider('あなたの今の調子は？',0 ,3000, 2000)
st.write('あなたのコンディション：', condition)

# サイドバーに追加
# 同一のウィジェットには同じ引数(表示文章)は指定できない
select_math_side = st.sidebar.selectbox(
    '①あなたの好きな数字を教えてください。',
    list(range(1, 11))
)
st.write('①あなたの好きな数字は',select_math_side, 'ですね' )

text_side = st.sidebar.text_input('②あなたの趣味を教えて下さい。')
'②あなたの趣味は：', text_side

condition_side = st.sidebar.slider('③あなたの今の調子は？',0 ,3000, 2000)
st.write('③あなたのコンディション：', condition_side)

# 2カラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ボタンが押されました')
    
# expander
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('回答を書く')

expander1 = st.expander('①問い合わせ')
expander1.write('①問い合わせ内容を書く')

expander2 = st.expander('②問い合わせ')
expander2.write('②問い合わせ内容を書く')

expander3 = st.sidebar.expander('質問')
expander3.write('回答')

# プログレスバー
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    #'経過時間',  i+1, '秒です' 変数に入れないと時間経過毎に行が増えていく
    bar.progress(i+1)
    time.sleep(1)
    
'Done!!'