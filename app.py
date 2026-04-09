import streamlit as st
import qrcode
from io import BytesIO

st.set_page_config(page_title="Ravi Tea QR")

# ---------------- LINK ----------------
APP_URL = "https://ravi-tea-rewards.streamlit.app"

# ---------------- UI ----------------
st.title("☕ RAVI TEA QR")
st.write("Scan to open rewards page")

# ---------------- QR GENERATION ----------------
qr = qrcode.make(APP_URL)

buf = BytesIO()
qr.save(buf)
buf.seek(0)

st.image(buf)

st.success("QR ready ✅")
