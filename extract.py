from PIL import Image

from sys import argv
from qrcode import make as makeQR

if __name__ == '__main__':
  im = Image.open(argv[1])
  s = w, h = im.size
  imd = im.load()
  
  oim = Image.new('1', s)
  oimd = oim.load()

  for i in range(w):
    for j in range(h):
      d = imd[i, j]
      oimd[i,j] = 255 if d[0] & 1 else 0

  from os.path import splitext
  root, ext = splitext(argv[1])
  oim.save(root+'_1bit'+ext)
