import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


class PDFReader:
    @staticmethod
    def extract(filepath: str) -> str:
        """Returns PDF pages content."""
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
