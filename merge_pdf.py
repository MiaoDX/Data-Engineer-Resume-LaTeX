from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()


dirname = ''
f1 = dirname+'template.pdf'
f2 = dirname+'template_zh_one_page.pdf'


input1 = open(f1, "rb")
input2 = open(f2, "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj = input1, pages = (0,1))
merger.append(fileobj = input2, pages = (0,1))

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

