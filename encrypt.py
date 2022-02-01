import os, sys
import base64
from time import sleep
from scipy import rand

key = input("Plz enter splitter phrase:")

for root, dirs, files in os.walk('G:/Python/image_cnry/f/input/'):
	for file in files:
		the_file=file
		if the_file=="decrypt.py" or the_file=="encrypt.py" or the_file=="convert_to_png":
			continue
		path = str('G:/Python/image_cnry/f/input/')
		f=open(path + the_file,"rb")
		plain_data=f.read()
		f.close()

		en_data = plain_data
		en_data = base64.b64encode(en_data)
		en_data = str(en_data)
	
		message = str(key)
		f = open("encrypted_list.txt","a")
		f.write(en_data)
		f.write(message)
		f.close()
        
print("Done!")
sys.exit() 