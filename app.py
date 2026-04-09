import streamlit as st
from io import BytesIO
from qr import generate_qr

st.title("☕ RAVI TEA QR")

APP_URL = "https://ravi-tea-rewards.streamlit.app"

# generate QR using qr.py
qr = generate_qr(APP_URL)

buf = BytesIO()
qr.save(buf)
buf.seek(0)

st.image(buf)

st.write("Scan to open rewards page")
