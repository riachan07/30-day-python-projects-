import qrcode as qgen

url = input("Enter URL: ")

qr = qgen.QRCode()
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code generated!")
