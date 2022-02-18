
import streamlit as st
import qrcode
from PIL import Image

st.title('QRコード自動生成アプリ')

if st.button('QRコードを生成'):
    _img = qrcode.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
    st.header("QRコード生成完了")
    st.balloons()
