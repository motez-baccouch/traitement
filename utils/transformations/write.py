from numpy import int32


def pgmwrite(img, filename, maxVal=255, magicNum='P2'):
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
      f.write(str(img[i][j]) + ' ')
      if count >= 17:
        # No line should contain gt 70 chars (17*4=68)
        # Max three chars for pixel plus one space
        count = 1
        f.write('\n')
      else:
        count = count + 1
    f.write('\n')
  f.close()


def ppmwrite(img, filename, maxVal=255, magicNum='P3'):
    (img, width, height) = img
    img = int32(img).tolist()
    f = open(filename + ".ppm", 'w')
    file = open(filename+".txt", "w+")
    content = str(img)
    file.write(content)
    file.close()
    f.write(magicNum + '\n')
    f.write(str(width) + ' ' + str(height) + '\n')
    f.write(str(maxVal) + '\n')
    for i in range(height):
        count = 1
        for j in range(width):
            f.write(str(img[i][j][0]) + ' '+str(img[i][j][1])+' '+str(img[i][j][2])+' ')
            # if count >= 17:
            #     # No line should contain gt 70 chars (17*4=68)
            #     # Max three chars for pixel plus one space
            #     count = 1
            #     f.write('\n')
            # else:
            #     count = count + 1
        f.write('\n')
    f.close()