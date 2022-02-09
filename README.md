# - Encryption
## How to :
- Choose a secret key (bigger is better) (I recommend more than 1024 characters)
- Just write full path when asked. (for input folder)
- And that it, you now got all ur file, encrypted in one text file !

# - Decryption 
## How to :
- Write the secret key you chose when encrypting
- Write all full paths. (for encrypted text file and output folder)
- Wait a bit if you have a lot of files
- And gg, you recovered your file!

# About
## Secret Key :
The private key is mixed with the base64 code, which means that the larger the key, the less likely it is to be in the base64 code.<br><br>
If the key is unfortunately in the base64 code, then some data cannot be recovered, this is why it is better to test the decryption with its secret key before deleting the non-encrypted data, and only keep the encrypted data.<br><br>
Clearly test your keys by decrypting before deleting the data to be encrypted.

## Supported file type :

Png, gif, jpg, jpeg, tiff, tif, bmp, raw.<br><br>
If you want more file types, please indicate them.
