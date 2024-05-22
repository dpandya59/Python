import hashlib
from difflib import SequenceMatcher

import os

def hashFile(file1,file2):
    h1=hashlib.sha1()
    h2=hashlib.sha1()

    with open(file1,"rb") as file:
        chunk=0
        while chunk !=b'':
            chunk= file.read(1024)
            h1.update(chunk)
    
    with open(file2,'rb') as file:
        chunk =0
        while chunk!=b'':
            chunk=file.read(1024)
            h2.update(chunk)
    
    return h1.hexdigest(),h2.hexdigest()

msg1,msg2=hashFile(os.path.join(r"C:\Users\Deepak Pandya\Documents\Learning\Python\Projects\PDFComparision\Phoniec.pdf"),os.path.join(r"C:\Users\Deepak Pandya\Documents\Learning\Python\Projects\PDFComparision\Phoniec.pdf"))

if msg1 == msg2:
    print("Files are identical")
else:
    print("Files are not identical")