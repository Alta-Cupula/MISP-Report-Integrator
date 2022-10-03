from os.path import isfile

import requests

from .docx import DOCXReader
from .pdf import PDFReader
from .report import ReportGenerator


class IOCExtractor(PDFReader, ReportGenerator):
    def extract_ioc(self, filepath: str = None, url: str = None) -> dict:
        """Extract content from file or url and uses a WebAPI for IOC extraction."""
        if filepath:

            if not isfile(filepath):
                exit(f"[!] File not found: {filepath}")

            extension = filepath.split(".")[-1]
            if extension in ("docx", "docm", "doc"):
                self.data = DOCXReader.extract(filepath).encode()
            elif extension == "pdf":
                self.data = PDFReader.extract(filepath).encode()
            return self.__fetch(_type="raw")
        elif url:
            self.data = {"url": url}
            return self.__fetch(_type="url")

    def __fetch(self, _type: str):
        """Fetch information about url or document."""
        if _type == "raw":
            api = "https://api.iocparser.com/raw"
            self.response = requests.request(
                "POST",
                url=self.api,
                headers={"Content-Type": "text/plain"},
                data=self.data,
            ).json()

        elif _type == "url":
            api = "https://api.iocparser.com/url"
            headers = {"Content-Type": "application/json"}
            self.response = requests.request(
                "POST",
                url=api,
                headers=headers,
                json=self.data,
            ).json()

        return self.response["data"]
