def set_max_height(img, maxHeight=500): 
    print(img.size)
    (width, height)= img.size
    aspect_ratio = width/height
    return img.resize(( int(maxHeight * aspect_ratio), maxHeight))