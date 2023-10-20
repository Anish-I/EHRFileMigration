import os
import pdfkit
from PyPDF2 import PdfFileMerger

class PDFMerger:
    def __init__(self, src_dir, pathpdf):
        self.src_dir = src_dir
        self.pathpdf = pathpdf
        self.pname = []

    def get_name(self):
        string_parts = self.src_dir.split('_')
        self.pname = (string_parts[2], string_parts[1])

    def convert_html_to_pdf(self):
        enc_folder = os.listdir(self.src_dir)
        for folder in enc_folder: 
            path = os.path.join(self.src_dir, folder)
            for html in os.listdir(path):
                if html.endswith(".html"):
                    # Convert HTML file to PDF
                    html_path = os.path.join(path, html)
                    pdf_file = os.path.splitext(html)[0] + ".pdf"
                    pdf_path = os.path.join(self.pathpdf, pdf_file)
                    try:
                        pdfkit.from_file(html_path, pdf_path)
                    except PermissionError:
                        print(f"Permission denied: {html_path}")
                        continue
                    except Exception as e:
                        print(f"Error occurred when converting {html} to PDF: {e}")
                        continue

    def merge_pdfs(self):
        output_dir = 'D:\\MergedHTMLs'  # replace with the path to your output folder
        output_filename = os.path.join(output_dir, self.pname[0] + "_" + self.pname[1] + "_ENC.pdf")  # replace with your desired output filename and path

        pdf_merger = PdfFileMerger()

        # Merge all PDF files in the folder into one document
        for filename in os.listdir(self.pathpdf):
            if filename.endswith('.pdf'):
                filepath = os.path.join(self.pathpdf, filename)
                with open(filepath, 'rb') as f:
                    pdf_merger.append(f)

        # Write the merged document to a new file in the output directory
        with open(output_filename, 'wb') as f:
            pdf_merger.write(f)

    def reset(self):
        for f in os.listdir(self.pathpdf):
            filepath = os.path.join(self.pathpdf, f)
            os.remove(filepath)

src_dir = "D:\\ProgressNotes"
pathpdf = "D:\\MergedPDFs"

merger = PDFMerger(src_dir, pathpdf)

for folder in os.listdir(src_dir):
    merger.src_dir = os.path.join(src_dir, folder)
    merger.get_name()
    merger.convert_html_to_pdf()
    merger.merge_pdfs()
    merger.reset()
