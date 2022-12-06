import calculators
import numpy as np
from numpy import int32

def egalisation(img,filename,maxVal=255, magicNum='P2'):
  hist = calculators.histo(img)
  cum = calculators.cumule(img)
  n1 = []
  for i in range(len(hist)):
    
    p = cum[i] / (img.shape[0] * img.shape[1])
    n1.append(int(np.floor(255*p)))

  # creating out
  out = []
  j = 0
  for i in range(len(hist) - 1):
    if(n1[j] == i):
      som = 0
      while(n1[j] == i):
        som = som + hist[j]
        j+=1
      out.append(som)
    else:
      out.append(0)

  print(out)

  # writing file
  img = int32(img).tolist()
  f = open(filename + ".pgm",'w')
  file = open(filename+".txt", "w+")
  content = str(img)
  file.write(content)
  file.close()
  width = 0
  height = 0
  for row in img:
    height = height + 1
    width = len(row)
  f.write(magicNum + '\n')
  f.write(str(width) + ' ' + str(height) + '\n')
  f.write(str(maxVal) + '\n')
  for i in range(height):
    count = 1
    for j in range(width):

      f.write(str(n1[img[i][j]]) + ' ')
      if count >= 17:
        # No line should contain gt 70 chars (17*4=68)
        # Max three chars for pixel plus one space
        count = 1
        f.write('\n')
      else:
        count = count + 1
    f.write('\n')
  f.close()