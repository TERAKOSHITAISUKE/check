from PIL import Image
import streamlit as st
import qrcode
import numpy as np
st.title('QRコード自動生成アプリ')

url = st.text_input('QRコードを生成したいURL:')

if st.button('QRコードを生成'):
    _img = qrcode.make(url)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
    st.header("QRコード生成完了")
    st.balloons()
