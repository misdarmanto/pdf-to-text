
import PyPDF2

def extract_text_from_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text
