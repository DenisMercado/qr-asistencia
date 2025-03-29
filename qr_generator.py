import qrcode

url="http://127.0.0.1:5000/asistencia"

img=qrcode.make(url)

img.save("qr_asistencia.png")