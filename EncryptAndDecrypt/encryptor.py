import sys, os, shutil
import struct
import hashlib, binascii
from Crypto.Cipher import AES
import passmaker, location_usb

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024) :
    """ 
    Encrypt a file using AES (CBC mode) with the given key.

    key:
        The encryption key - a string that must be either 16, 
        24 or 32 bytes long. Longer keys are more secure.abs
    in_filename:
        Name of the input file

    out_filename:
        If None, '<in_filename>.enc' will be used.abs

    chunksize:
        Sets the size of the chunk which the function uses to
        read and encrypt the file. Larger chuck sizes can be 
        faster for some files and machines. 
        chunksize must be divisible by 16.
    """

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = 'carinusteam12345'
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

            return out_filename

def main() :
    #password to key
    password = passmaker.make_pass()
    key = hashlib.sha256(password).digest()
    print binascii.hexlify(bytearray(key))

    #encrypt file
    in_filename = sys.argv[1]
    copy_source = encrypt_file(key, in_filename, out_filename=None)
    print 'Encrypt Done !'

    #delete original file
    #os.remove(in_filename)
    
    #Copy backup file to USB disk
    shutil.copy(copy_source, location_usb.getLocation())    

main()