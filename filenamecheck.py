#from __future__ import print_function

import os, sys, os.path
import fpdf
print(sys.version)

counter = 0
pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
filepath = input("Enter file path here: ")

while True and counter < 2:
    if os.path.exists(filepath):
        filename = input("Enter file name here: ")

        file_counting = 0

        for file in os.listdir(filepath):

            if file.startswith(filename.upper()) or file.startswith(filename.lower()):
                pdf.write(5, file)
                pdf.ln()
                file_counting += 1
                s = str(file_counting)

        pdf.write(5, 'Total files found: ')
        pdf.write(5, s)

    pdfname = input("Enter what you want to name your pdf with extension: ")
    pdf.output(pdfname)

    if not os.path.exists(filepath):
        print("Please enter a valid file path or check for errors")
        filepath = input("Enter file path here: ")
        counter += 1

else:
    print("Max incorrect entries reached. Please restart the program.")
    sys.exit(1)
