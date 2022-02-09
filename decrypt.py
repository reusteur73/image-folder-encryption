import os, sys
import base64

# Ask for user input
key = str(input("Please enter secret key:")) # Ask for secret key
inn = input('Please enter full path of encrypted txt file:') # Ask for encrypted file path
out = input('Please enter full path of output folder:') # Ask for output folder path
out += '\\' # Format path

f=open(inn,"r") # Open encrypted data file
plain_data=f.read() # Define it
f.close() # Close

not_traited_data = plain_data.replace(key, "\n") # Replace the key with return 
f=open("temp_decrypted_data.txt","a") # Create and open a decrypted data temporary file txt
f.write(not_traited_data) # Write our data
f.close() # Close

# Entension definition
png = base64.b64encode("png".encode()).decode() # Define encoded png
gif = base64.b64encode("gif".encode()).decode() # Define encoded gif
jpg = base64.b64encode("jpg".encode()).decode() # Define encoded jpg
jpeg = base64.b64encode("jpeg".encode()).decode() # Define encoded jpeg
tiff = base64.b64encode("tiff".encode()).decode() # Define encoded tiff
tif = base64.b64encode("tif".encode()).decode() # Define encoded tif
bmp = base64.b64encode("bmp".encode()).decode() # Define encoded bmp
raw = base64.b64encode("raw".encode()).decode() # Define encoded raw


file1 = open("temp_decrypted_data.txt", 'r') # Open decrypted data txt
Lines = file1.readlines() # Get lines
file1.close()
count = 0 # Initialise counter 

#For each line :
for line in Lines: # Create the loop for each line
    extension = "" # Reset extension type
    count += 1 # Add one to file counter

    # If png is detect, remove it and set extension as .png
    if png in line:
        line.replace(png, '')
        extension = ".png"
    # If gif is detect, remove it and set extension as .gif
    if gif in line:
        line.replace(gif, '')
        extension = ".gif"
    # If jpg is detect, remove it and set extension as .jpg
    if jpg in line:
        line.replace(jpg, '')
        extension = ".jpg"
    # If jpeg is detect, remove it and set extension as jpeg
    if jpeg in line:
        line.replace(jpeg, '')
        extension = ".jpeg"
    # If tiff is detect, remove it and set extension as tiff
    if tiff in line:
        line.replace(tiff, '')
        extension = ".tiff"
    # If tif is detect, remove it and set extension as tif
    if tif in line:
        line.replace(tif, '')
        extension = ".tif"
    # If bmp is detect, remove it and set extension as bmp
    if bmp in line:
        line.replace(bmp, '')
        extension = ".bmp"
    # If raw is detect, remove it and set extension as raw
    if raw in line:
        line.replace(raw, '')
        extension = ".raw"

    name = str(count) + extension # Define name
    
    x = line.encode() # Encode the line to decodeB64
    en_data2 = base64.b64decode(x) # Decode B64
    
    f = open(out + name, "wb") # Create and open final decrypted file
    f.write(en_data2) # Write data file
    f.close # Close

os.remove("temp_decrypted_data.txt") # Delete decrypted data temporary file
print("Done, decrypted " + str(count) + ' files!') # Print end
sys.exit() # Quit 
