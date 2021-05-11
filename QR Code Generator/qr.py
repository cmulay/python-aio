import pyqrcode

filename = input('What is this QR Code Generator for: ')
get_details = input('Link or Text to generate QR from : ')
qr = pyqrcode.create(get_details)
qr.svg(f'{filename}.svg', scale=8)
