from PIL import Image

from sys import argv
from qrcode import make as makeQR

if __name__ == '__main__':
  qr = makeQR(argv[1])
  qw, qh = qr.size

  im = Image.open(argv[2])
  w, h = im.size

  imd = im.load()
  for i in range(w):
    for j in range(h):
      d = imd[i, j]
      imd[i, j] = ((d[0] | 1) if qr.getpixel((i%qw, j%qh)) else (d[0] & 254), *d[1:])

  from os.path import splitext
  root, ext = splitext(argv[2])
  im.save(root+'_watermark'+ext)
  #qr.save(root+'_qrcode'+'.png')
