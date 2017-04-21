#!/usr/bin/env python

import PyPDF2
import docx
import sendBraille
from Tkinter import Tk
from tkFileDialog import askopenfilename

def extractPdf(input_file):
    pdf_file = open(input_file, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    final_content = ""
    for i in range(number_of_pages):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        page_content = page_content.replace("\n", "")
        final_content = final_content + page_content
    return final_content.encode('utf-8')

def extractDocx(input_file):
    doc = docx.Document(input_file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def extractText(input_file):
    doc = open(input_file)
    fullText = ""
    for line in doc :
        fullText = fullText + line
    return fullText

#print extractDocx("res/sample_multiple.docx")
#print extractPdf("res/sample_multiple.pdf")
#print extractText("res/sample.txt")
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
input_file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
page_content = ""
try:
    if(input_file.endswith(".pdf")) :
        page_content = extractPdf(input_file)
    elif(input_file.endswith(".docx")) :
        page_content = extractDocx(input_file)
    elif(input_file.endswith(".txt")) :
        page_content = extractText(input_file)
    else :
        print "Please select valid PDF, DOCX, TXT file.\n"
except (IOError) :
    print "No Such file Found"

try:
    sendBraille.recieve_content(page_content)
except :
   print "Something Bad Happened"
raw_input("Press Enter To Exit")

