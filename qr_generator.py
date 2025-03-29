import qrcode

url="https://qr-asistencia.onrender.com/asistencia"

img=qrcode.make(url)

img.save("qr_asistencia.png")