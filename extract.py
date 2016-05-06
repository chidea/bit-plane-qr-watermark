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
      oimd[i,j] = 255 * (d[-1] & 1)
      #oimd[i,j] = 255 * (d[-1]>>1 & 1)
      #oimd[i,j] = 255 * (1 if d[-1] & 0b111 == 0b111 else 0)

  from os.path import splitext
  root, ext = splitext(argv[1])
  fname = root+'_1bit'+ext
  oim.save(fname)
  from sys import platform
  if platform == 'win32':
    from os import startfile
    startfile(fname)
  elif platform == 'darwin':
    from os import system
    system('open '+fname)
  elif platform.startswith('linux'):
    from os import system
    system('xdg-open '+fname)
