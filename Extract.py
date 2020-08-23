#Extract the text file from the image
from PIL import Image
import bitarray
#Steganography
def convert(list): 
    # Converting integer list to string list 
    s = [str(i) for i in list] 
    # Join list items using join() 
    res = int("".join(s)) 
    return(res)

def rgb_to_char(r,g,b) :
    numBins = []
    bit_of_r = list(map(int,(format(r, '08b'))))
    bit_of_g = list(map(int,(format(g, '08b'))))
    bit_of_b = list(map(int,(format(b, '08b'))))
    numBins = numBins + bit_of_r[5:]
    numBins = numBins + bit_of_g[5:]
    numBins = numBins + bit_of_b[6:]
    s = ""
    for i in numBins:
        s+=str(i)
    n=int(s,2)
    ss =chr(n)
    if(n<=127) : # ascii range
        data = bitarray.bitarray(s).tobytes().decode('utf-8')
        return data
    else:
        return  " "
    

imagefile = Image.open('Embedded_img_1.png')
pixi_out2 = list(imagefile.getdata())
imagefile.close()
length = pixi_out2[0]
file_size=pixi_out2[1]
numBins = []
cnt = -1
for i in length :
    bits = list(map(int,(format(i, '08b'))))
    cnt+=1
    if cnt <2 :
        numBins = numBins+bits[5:]
    else :
        numBins = numBins+bits[6:]
 
s = convert(numBins)
data = int(str(s),2)
print("File name length => ",data)

#get file size
numBins = []
for i in file_size:
    bits = list(map(int, (format(i, '08b'))))
    numBins = numBins + bits
s = convert(numBins)
data1 = int(str(s), 2)

file_size = data1
#Extract the name of file

file_name = "Extracted_"


for i in range(2,data+2) :
	tup = pixi_out2[i] 
	r = tup[0]
	g = tup[1]
	b = tup[2]
	file_name+=(rgb_to_char(r,g,b))
	
print("Extracted File Name = > ",file_name)
loopRun = data+2+file_size
f = open(file_name,'w')
for i in range(data+2,loopRun) :
    tup = pixi_out2[i]
    r,g,b = tup[0],tup[1],tup[2]
    char = rgb_to_char(r,g,b)
    f.write(char)

print("\n____________________________")
print(" Extraction Complete !!")
print("____________________________")
