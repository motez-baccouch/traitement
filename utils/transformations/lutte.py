import math
from numpy import int32

def lutte(a, b ,filename, img , maxVal=255, magicNum='P2' ): 

  """
  uses read_pgm and writes by itself
  """

  pente1= math.floor(a["y"]/a["x"])
  pente2 = math.floor((b["y"]-a["y"] )/ (b["x"]-a["x"]))
  pente3 = math.floor((255-b["y"])/(255-b["x"]))

  b2 = a["y"] - pente2*a["x"]
  b3 = b["y"] - pente3*b["x"]


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
      if(img[i][j] <= a["x"]): 
        val = pente1 * img[i][j]
      elif(img[i][j]>a["x"] and img[i][j]<b["x"] ): 
        val= pente2 * img[i][j]+b2
      else:
        val= pente3 * img[i][j]+ b3
      f.write(str(val) + ' ')
      if count >= 17:
        # No line should contain gt 70 chars (17*4=68)
        # Max three chars for pixel plus one space
        count = 1
        f.write('\n')
      else:
        count = count + 1
    f.write('\n')
  f.close()