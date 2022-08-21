import io
import resource
from pprint import pprint as pp

import requests
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

# def extract_text_by_page(pdf_path):
#     with open(pdf_path, 'rb') as fh:
#         text = ""
#         for page in PDFPage.get_pages(fh,
#                                     caching=True,
#                                     check_extractable=True):
#             resource_manager = PDFResourceManager()
#             fake_file_handle = io.StringIO()
#             converter = TextConverter(resource_manager,
#                                     fake_file_handle)
#             page_interpreter = PDFPageInterpreter(resource_manager,
#                                                 converter)
#             page_interpreter.process_page(page)
#             text += fake_file_handle.getvalue()
            
#             yield text
            
#             # close open handles
#             converter.close()
#             fake_file_handle.close()
            
# def extract_text(pdf_path):
#     data = ""
#     for page in extract_text_by_page(pdf_path):
#         data += page

#     extract_ioc(data)

def extract(filepath: str) -> str:
    with open(filepath, "rb") as doc:
        text = ""
        manager = PDFResourceManager()
        handler = io.StringIO()
        converter = TextConverter(manager, handler)
        interpreter = PDFPageInterpreter(manager, converter)

        for page in PDFPage.get_pages(doc):
            interpreter.process_page(page)
            text += handler.getvalue()
    
    return text

def extract_ioc(data: str) -> None:
    api = "https://api.iocparser.com/raw"
    headers = {"Content-Type": "text/plain"}

    response = requests.request(
        "POST",
        url=api,
        headers=headers,
        data=data.encode(),
    ).json()

    pp(response)

# Driver code
if __name__ == '__main__':
    print(extract('pdf/bruh.pdf'))
