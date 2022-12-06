from numpy import array

def pgmread(filename):
  f = open(filename,'r')
  # Read header information
  count = 0
  while count < 3:
    line = f.readline()
    if line[0] == '#': # Ignore comments
      continue
    count = count + 1
    if count == 1: # Magic num info
      magicNum = line.strip()
      if magicNum != 'P2' and magicNum != 'P5':
        f.close()
        print('Not a valid PGM file')
        exit()
    elif count == 2: # Width and Height
      [width, height] = (line.strip()).split()
      width = int(width)
      height = int(height)
    elif count == 3: # Max gray level
      maxVal = int(line.strip())
  # Read pixels information
  img = []
  buf = f.read()
  elem = buf.split()
  if len(elem) != width*height:
    print('Error in number of pixels')
    exit()
  for i in range(height):
    tmpList = []
    for j in range(width):
      tmpList.append(elem[i*width+j])
    img.append(tmpList)
  return (array(img), width, height)


def ppmread(filename):
    f = open(filename, 'r')
    # Read header information
    count = 0
    while count < 3:
        line = f.readline()
        if line[0] == '#':  # Ignore comments
            continue
        count = count + 1
        if count == 1:  # Magic num info
            magicNum = line.strip()
            if magicNum != 'P3':
                f.close()
                print('Not a valid PPM file')
                exit()
        elif count == 2:  # Width and Height
            [width, height] = (line.strip()).split()
            width = int(width)
            height = int(height)
        elif count == 3:  # Max gray level
            maxVal = int(line.strip())

    # Read pixels information
    img = []
    buf = f.read()
    elem = buf.split()
    print(elem)
    if len(elem) != width*height*3:
        print('Error in number of pixels')
        exit()
    for i in range(height):
        tmpList = []
        print(elem[i*width*3])
        for j in range(width):
            colorList = []
            for k in range(0, 3):
                colorList.append(elem[i*width*3+j*3+k])
            tmpList.append(colorList)
        img.append(tmpList) 

    return (array(img), width, height)