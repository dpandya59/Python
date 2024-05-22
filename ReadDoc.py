import docx
import os
def getFileText(fileName):
    doc = docx.Document(fileName)
    fullText = []
    fulltext=""
    for para in doc.paragraphs:
        fulltext+=para.text
        fullText.append(para.text)
    #print(fulltext)
    # return '\n'.join(fullText)

getFileText(os.path.join(r"C:\Users\Deepak Pandya\Documents\Personal\Resume\Deepak_Pandya.docx"))
