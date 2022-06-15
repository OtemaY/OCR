#Read multiple PDF files, looking for specific word
import csv
import glob
import pandas

result_list = []
search_term = "TOTAL"



f = open(f'files3.csv',mode='w')
for i in glob.glob('/Users/otemayirenkyi/Downloads/'folder'/*.pdf'):   #search in file path 
    f_writer = csv.writer(f)
    

    
    with pdfplumber.open(i) as pdf:
        for page_number in range(0, len(pdf.pages)):
            page = pdf.pages[page_number].extract_text()

            page = page.split('\n')
         
            for line in page:
                if search_term in line:
                    words = line.split()
                    print(words)
                    f_writer.writerow(words)
                    
                    result = {
                    "page": page_number,
                    "content": line
                    }
           

            result_list.append(result)

        results = {
            "file": i,
            "results": result_list
        }
#         print(results)
f.close()
new = pd.DataFrame.from_dict(results)
        
new
