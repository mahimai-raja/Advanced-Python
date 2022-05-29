import pyqrcode

String = 'https://github.com/mahimai-raja'

Url = pyqrcode.create(String)

# remember to save only on SVG format

Url.svg('QR_Code.svg', scale = 6)   

''' 
Okay now you a intresting work !
Find out how to convert this SVG file to PNG file 

Do comment below ->
'''