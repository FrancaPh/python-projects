from pyzbar.pyzbar import decode
from PIL import Image

path = input('What\'s the name of the file?\n')

decocdeQR = decode(Image.open(path + '.png'))

print(decocdeQR[0].data.decode('ascii'))