import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/watch?v=XCsViS_ra7U"

url = pyqrcode.create(s)

url.svg("youtube.svg", scale=8)
