import pdftotext

with open("/Users/evangrandfield/nlp_project/bib/HBible.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
    for i in range(100, 102):
        print(pdf[i]) 

with open('HBible.txt', 'w') as f:
    f.write("\n\n".join(pdf))
