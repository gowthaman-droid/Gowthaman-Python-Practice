import qrcode
a=input("Give a link to generate to Qr code: ")
data=a

qr=qrcode.make(data)
qr.show()