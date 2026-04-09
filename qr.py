import qrcode

# 🔗 Your App Link
data = "https://ravi-tea-rewards.streamlit.app"

qr = qrcode.make(data)

qr.save("ravi_tea_qr.png")

print("QR Generated")
