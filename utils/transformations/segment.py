
def segement(img, seuil=255, method="ET"):

    """
    uses pgmreact and pgmwrite
    """

    (imgMatrix, width, height) = img

    generatedImg = []
    for i in range(height):
        generatedLine = []
        line = imgMatrix[i]
        for j in range(width):
            pixelToAdd = []
            pixel = line[j]
            if(method=="ET"):
                pixelToAdd= checkPixelEt(pixel, seuil)
            else: 
                pixelToAdd= checkPixelOu(pixel, seuil)
            generatedLine.append(pixelToAdd)
        generatedImg.append(generatedLine)

    return (generatedImg, width, height)

def checkPixelEt(pixel,seuil=255):
    for k in range(3):
        if(int(pixel[k]) < seuil): 
            return ['0','0','0']
    return ['255','255','255']

def checkPixelOu(pixel, seuil=255):
    for k in range(3):
        if(int(pixel[k]) > seuil):
            return ['255','255','255']
    return ['0','0','0']