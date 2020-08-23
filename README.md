# Steganography using Python

Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination. The use of steganography can be combined with encryption as an extra step for hiding or protecting data. The word steganography is derived from the Greek words steganos (meaning hidden or covered) and the Greek root graph (meaning to write).

Steganography can be used to conceal almost any type of digital content, including text, image, video or audio content; the data to be hidden can be hidden inside almost any other type of digital content. The content to be concealed through steganography -- called hidden text -- is often encrypted before being incorporated into the innocuous-seeming cover text file or data stream. If not encrypted, the hidden text is commonly processed in some way in order to increase the difficulty of detecting the secret content.

In this project, this technique is implemented by hiding a text file inside an image  :
![](trees.jpg)

_____________________________________________________________________________________________
Following are the steps : -
#### Steganography.py

1. Load the image and calculate its capacity of storing characters( heigthxwidth),
    idea is to store 1 character in 1 pixel of the image.
2. Extract the name of the file (i.e, embedder.txt) and convert it to byte-array.
3. Calculate the size of the file and trasform it to bits of 24 length(RGB - 8 bits for each ).
4. Now, Read 1 character from file, convert it to bits.
5. Slice the bits into 3,3 & 2 size and modify the LSBs(least significant bits) of RGB of each pixel.
6. Repeat till all characters of filename and the file itself are finished.
7. Save the new pixels in .png format to avoid lossy compression.
8. Close the image.

#### Extract.py

1. Load image (i.e, Embedded_img_1.png).
2. Extract RGB values from first pixel and using this get the file name length.
3. Extract RGB values from second pixel and using this get the file size.
4. From 3rd pixel onward till file name length, convert each RGb to char(using rgb_to_char method)
    and form the new name of the file as Extracted_filename.txt
5. Open the file in above step in "write" mode.
6. Now, till counter reaches file size,using rgb_to_char method, write characters to file
7. Save it and close the image.

_________________________________________________________________________________________________________

The new image having data of file hidden in it, doesn't seems to be affected at all 
and is almost identical to the input image, trees.jpg
![](Embedded_img_1.png)
