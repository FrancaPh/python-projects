import qrcode

data = input('what do you want to encode in QR code?\n')
path = input('What\'s the name of the file?\n')

img = qrcode.make(data)
img.save(path + '.png')

print('QR code Generated!')