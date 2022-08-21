import requests

from .reader import PDFReader
from .report import ReportGenerator


class IOCExtractor(PDFReader, ReportGenerator):
    def __init__(self) -> None:
        self.api = "https://api.iocparser.com/raw"  
        self.headers = {"Content-Type": "text/plain"}

    def extract_ioc(self, filepath: str) -> dict:
        """Extract content from PDF file and uses a WebAPI for IOC extraction."""
        self.data = PDFReader.extract(filepath).encode()

        print("[+] Extracting document IOCs")
        self.response = requests.request(
            "POST",
            url=self.api,
            headers=self.headers,
            data=self.data,
        ).json()

        return self.response['data']
