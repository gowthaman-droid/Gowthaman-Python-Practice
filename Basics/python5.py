import qrcode
data='https://www.istockphoto.com/photos/couple-love-hearts'
qr=qrcode.make(data)
qr.show()