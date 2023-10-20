# EHRFileMigration

In this project, I worked with a doctor who had a problem with migrating files between EHRs (electronic Health Records) which are stored in a thumb drive with thousands of other patients that aren't hers. With this apprent mess, she was able to get an excel file of all the names of her patients within the thumb drive, and from there the code takes off.

FileExporter.ipynb
-------------------
This file has many capabilities in which takes all the names from the excel sheet and makes it into a tuple, but the problem with the excel sheet was it wasn't converted properly and names with jumbled with their birthdays and gender mark as "M or F". The code uses the tuple to search the main drive in which copied the files, and moved it into another flash drive in which will come in handy later. Most of this code has a lot of debuggers, and file transfers as I used many excel sheets to extract the data from. This successfully traversed through many folders patient names, and found them and pasted into a flash drive, and this also compared what has been done, and what hasn't been done with excel files.

FileMerger.py
----------------
Import Required Modules:

The script starts by importing the necessary modules: os, pdfkit, and PdfFileMerger from the PyPDF2 library.
Define PDFMerger Class:

The script defines a class named PDFMerger.
The constructor (__init__) initializes the class with source directory (src_dir) and PDF output directory (pathpdf).
The pname attribute is used to store parts of a name extracted from the source directory.
get_name Method:

The get_name method extracts parts of a name from the src_dir and stores them in the pname attribute. It assumes that the src_dir follows a naming convention with underscores, and it retrieves the second and third parts.
convert_html_to_pdf Method:

The convert_html_to_pdf method goes through each folder within the src_dir.
For each HTML file within these folders, it converts the HTML to a PDF using the pdfkit.from_file function.
The converted PDF files are saved in the pathpdf directory.
Any exceptions that occur during the conversion process are caught and handled, printing relevant error messages.
merge_pdfs Method:

The merge_pdfs method is responsible for merging all the PDF files in the pathpdf directory into a single PDF file.
It uses the PdfFileMerger class from PyPDF2 to achieve this.
The merged PDF is then saved in a specified output directory with a filename generated from the extracted name parts.
reset Method:

The reset method is designed to delete all PDF files within the pathpdf directory. It is intended to clean up the PDFs after they have been merged.
Main Loop:

The main part of the script iterates through each folder in the src_dir.
For each folder, it updates the src_dir attribute of the merger object and calls the get_name, convert_html_to_pdf, merge_pdfs, and reset methods in sequence.
This loop essentially processes each folder's HTML files, converts them to PDFs, merges the PDFs, and then clears the PDFs.
Overall, this script seems to be intended for converting HTML files into PDFs, merging those PDFs, and organizing the output based on a specific naming convention. It looks like it's meant to process progress notes in HTML format and create a consolidated, merged PDF output for each set of progress notes.




