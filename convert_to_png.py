# Python code to
# demonstrate readlines()
import os, sys
import base64




 
# Using readlines()
file1 = open('decypted_data.txt', 'rb')
Lines = file1.readlines()

path = str("G:/Python/image_cnry/f/output/")

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    name = str(count) + ".png"
    f = open(path + name, "wb")
    en_data = base64.b64decode(line)
    f.write(en_data)
    f.close
print("Done.")