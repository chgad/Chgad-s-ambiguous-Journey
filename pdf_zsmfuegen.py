from PyPDF2 import PdfFileMerger
import natsort
import os

DIR = r"C:\Users\Christian\Downloads"
OUTPUT = "ex2_Praesenz.pdf"

file_list = filter(lambda f: f.startswith('Prae'), os.listdir(DIR))
file_list = natsort.natsorted(file_list)

# 'strict' used because of
# https://github.com/mstamy2/PyPDF2/issues/244#issuecomment-206952235
merger = PdfFileMerger(strict=False)

for f_name in file_list:
    f = open(os.path.join(DIR, f_name), "rb")
    merger.append(f)

output = open(OUTPUT, "wb")
merger.write(output)


