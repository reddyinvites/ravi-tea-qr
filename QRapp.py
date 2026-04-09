# ---------------- QR CODE ----------------
import qrcode
from io import BytesIO

st.subheader("📲 Scan & Start")

APP_URL = "https://ravi-tea-rewards.streamlit.app"

qr = qrcode.make(APP_URL)

buf = BytesIO()
qr.save(buf)
buf.seek(0)

st.image(buf, width=250)

st.download_button(
    label="⬇️ Download QR",
    data=buf,
    file_name="ravi_tea_qr.png",
    mime="image/png"
)
