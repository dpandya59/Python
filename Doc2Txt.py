from docx import Documents
import os
import shutil
import io

def convertDoxToText(docFilename):
    # docx2txt.process("C:\\Users\\Deepak Pandya\\Documents\\Personal\\Resume\\Deepak_Pandya.doc")
     document = Documents(docFilename)
     textFilename=os.path.join(r"C:\Users\Deepak Pandya\Documents\Personal\Resume\Deepak_Pandya",".txt")
     with io.open(textFilename,'w',encoding='utf-8')as textifile:
         textFilename.write(docx2txt.process(docFilename))

docFileName=os.path.join(r"C:\Users\Deepak Pandya\Documents\Personal\Resume\Deepak_Pandya",".doc")
convertDoxToText(docFileName)
