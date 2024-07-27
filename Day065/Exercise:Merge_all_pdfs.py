"""
Objective :
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.
"""
import os
import shutil
import string
from pypdf import PdfMerger

if (not os.path.exists("productFolder")):
  os.mkdir("Day065/productFolder")

PDFbin = os.listdir("Day065/rawPDFs")
for file in PDFbin:
  if file.endswith(".pdf"):
    shutil.copy2(f"Day065/rawPDFs/{file}",f"Day065/productFolder")

unmodifiedFiles = os.listdir("Day065/productFolder")
for count,file in enumerate(unmodifiedFiles):
  os.rename(f"Day065/productFolder/{file}",f"Day065/productFolder/{string.ascii_letters[count]}.pdf")

modifiedFiles = os.listdir("Day065/productFolder")
merger = PdfMerger()
for pdf in modifiedFiles:
  merger.append(f"Day065/productFolder/{pdf}")

merger.write("Day065/productFolder/merged-pdf.pdf")
merger.close()