# Reading from multiple PDF files at a time with pdfplumber

#pip install the pdfplumber library
pip install pdfplumber

#pip install the glob library
pip install glob2

import glob
import pdfplumber

file_path = '/Users/otemayirenkyi/Downloads/'folder'/*.pdf'

txt_file = open("test6.txt",mode='a',encoding='utf-8')
    
for file in glob.glob(file_path):
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
    print('\n')
    print(txt)

           
    txt_file.write(txt)
            
txt_file.close()

print('\n')
print("Success")
