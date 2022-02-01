import os, sys
import base64

from rsa import encrypt

key = input("Please enter the key:")
final_key = str(key)
f=open("encrypted_list.txt","r")
plain_data=f.read()
f.close()
first = "'" + final_key + "b'"
deux = "'" + final_key
not_traited_data = plain_data.replace(first, "\n")

not_traited_data = not_traited_data.replace("b'", "")
final_data = not_traited_data.replace(deux, "")
f=open("decypted_data.txt","a")
f.write(final_data)
f.close()

    
print("Done!")
sys.exit() 