from PIL import Image
import os
import numpy as np
#Steganography

def convert(list):
    # Converting integer list to string list 
    s = [str(i) for i in list] 
    # Join list items using join()
    res = int("".join(s)) 
    return(res)

# locate the file
filename = "embedder.txt"
# open the file
imbeddingFile = open(filename,"r")

d = filename.split(sep="\\")
# just store the file name(with extension)
name = d[::-1][0]

imagefile = Image.open("trees.jpg")
# get dimensions of the image
width, height = imagefile.size
# number of characters image can store
capacity = width * height
print(" Capacity => ",capacity)
# get size of the file
filesize = os.path.getsize(filename)

if (capacity <= filesize ):
    print(" Sorry ! File can't be embedded")
else :
    print(" File can be embedded, size  =>  ",filesize)

# get all pixels in RGB value as a list
original_pixels = list(imagefile.getdata())
# convert name of file into byte
nameByte = list(bytes(name, "utf-8"))
# Store all characters of file as byte in byte numpy array
Bytes = np.fromfile(filename, dtype = "uint8")
# output pixel matrix
Modified_pixels = []
name_len = len(name)
total_chars = len(Bytes)
loopRun = total_chars+name_len+2# : first 2 pixels are reserved for length filename & file size

# Lambda expresson for converting an integer to bits of n length
get_bin = lambda x, n: format(x, 'b').zfill(n)

capacity_bits = list(map(int,get_bin(filesize,24)))
#counter
cnt = -1

for i in range(loopRun) :
    cnt+=1
    rgb = [] # empty R,G,B list
    all_bits = [] # empty R,G,B bits list

    if i == 0 :
        all_bits = list(map(int,get_bin(name_len,8))) # convert length of filename to bits
    # use whole 2nd Pixel to store file size in bits
    if i==1 :
        r = capacity_bits[:8]
        s = convert(r)
        data1 = int(str(s), 2)
        g = capacity_bits[8:16]
        s = convert(g)
        data2 = int(str(s), 2)
        b = capacity_bits[16:24]
        s = convert(b)
        data3 = int(str(s), 2)
        Modified_pixels.append(tuple([data1,data2,data3]))
        continue
    # from 3rd pixel onward store characters of file name in each pixel
    if i>1 and i <= (name_len)+1  :
        j = i - 2
        byte = nameByte[j]
        all_bits = list(map(int,(format(byte, '08b'))))

    # After file name is stores, embed file characters in each pixel
    if i >= (name_len+2):
        j = i - 2 - name_len
        byte = Bytes[j]
        all_bits = list(map(int,(format(byte, '08b'))))

        
 
    r = (all_bits[:3]) # will go in Red band
    g = (all_bits[3:6])# will go in Green band
    b = (all_bits[6:])# will go in Blue band
    rgb.append(r)
    rgb.append(g)
    rgb.append(b)
    tup = original_pixels[cnt] # get current RGB tuple e.g (5,65,153)
    new_tuple = [] # to store modified value of RGB tuple e.g (3,66,154)
    for dig in range(len(tup)) : # dig is a counter 0,1,2
        modi = []
        Bit = list(map(int,(format(tup[dig], '08b'))))
        if dig != 2 : # R band stores 3 bits, G band stores 3 bits & B band stores 2 bits
            modi = Bit[:5] + rgb[dig]
            s = convert(modi)
            data = int(str(s),2)
            new_tuple.append(data)
        else:
            modi = Bit[:6] + rgb[dig]
            s = convert(modi)
            data = int(str(s),2)
            new_tuple.append(data)
    Modified_pixels.append(tuple(new_tuple))

# add the remaining pixels    
Modified_pixels = Modified_pixels + original_pixels[loopRun:]

# Use PIL to create an image from the new array of pixels
image_out = Image.new(imagefile.mode,imagefile.size)
imagefile.close()
image_out.putdata(Modified_pixels)
image_out.save("Embedded_img_1.png")
image_out.close()
print("\n____________________________")
print(" Embedding Complete !!")
print("____________________________")
