import os, sys
import base64

# Ask user input
key = input("Please enter secret key (at least 512 character is recommended):") # Ask for secret key
folder = input('Please enter full path of folder to encrypt :')  # Ask for folder that contain files to encrypt
folder += '\\' # Format path input

# Define loop option
counter = 0 # Initialise file counter
ff = open("encrypted_list.txt","a") # Open the output txt file
for root, dirs, files in os.walk(folder): 
	for file in files: # For each file :
		counter +=1 # Add one to the file counter
		the_file=file
		if the_file=="decrypt.py" or the_file=="encrypt.py" or the_file=="convert_to_png": # If script is in this folder skip
			continue
# Data encoding
		extension = file.split('.', 1) #split file name after '.' to get extension type 
		extension = base64.b64encode(extension[1].encode()).decode() # Encode extension type
		f=open(folder + the_file,"rb") # Open the file
		plain_data=f.read()  # Read and define file data
		f.close() # Close file

		en_data = base64.b64encode(plain_data).decode()  # B64 encode file data
	
# Data writing 
		ff.write(en_data) # Write encoded file data
		ff.write(extension) # Write encoded extension type
		ff.write(key) # Write Secret key 
		 
ff.close() # Close output file
print("Done, encrypted "+ str(counter) + " files") # Print end
sys.exit() # Quit
