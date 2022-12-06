from numpy import int32
import math

def pgm_filtre_mediane(img, filename, maxVal=255, magicNum="P2", filterSize=3):

    img = int32(img).tolist()

    f = open(filename + ".pgm", 'w')
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
            if i > height-math.floor(filterSize/2) or j > width-math.floor(filterSize/2) or i < math.floor(filterSize/2) or j < math.floor(filterSize/2):
                f.write(str(img[i][j])+" ")

            else:
                tab= []
                for k in range(math.ceil(-filterSize/2), math.floor(filterSize/2)):
                    for y in range(math.ceil(-filterSize/2), math.floor(filterSize/2)):
                        tab.append(img[i+k][j+y])

                tab.sort()
                f.write(str(tab[math.floor(len(tab)/2)])+ " ")

            if count >= 17:
                # No line should contain gt 70 chars (17*4=68)
                # Max three chars for pixel plus one space
                count = 1
                f.write('\n')
            else:
                count = count + 1
        f.write('\n')
    f.close()

    return