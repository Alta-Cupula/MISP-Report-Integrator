import json
import sys
from pprint import pprint as pp

import requests
from PyPDF2 import PdfFileReader

# TODO: Add differente output types (json, xml, yml) for different program imports
# TODO: Add URL scan option to upload and scan files online
# BUG: PDF reading can be really messed up, sometimes even causing errors in the code, but the cause is unknown


class IOCExtractor:
    def __init__(self):
        self.api = "https://api.iocparser.com/raw"

    def parse_document(self, filepath: str):
        """Read given document and prepare information for futher usage."""
        try:
            file = open(filepath, "rb")
            reader = PdfFileReader(file)
            page_count = reader.getNumPages()
            print(f"[+] Loaded file has {page_count} page(s)")

            self.content = ""
            for idx in range(page_count):
                page = reader.getPage(idx)
                self.content += str(page.extractText(page)).replace(" ", "")
                pp(self.content)
                return self.content
        except FileNotFoundError:
            print(f"[!] File not found: {filepath}")
            sys.exit(1)

    def extract_ioc(self, filepath: str):
        self.headers = {"Content-Type": "text/plain"}
        self.data = self.parse_document(filepath)

        print("[+] Extracting IOCs in file")
        self.response = requests.request(
            "POST",
            url=self.api,
            headers=self.headers,
            data=self.data,
        ).json()

        print(json.dumps(self.response, indent=4))

        with open("output.json", "w") as output:
            json.dump(self.response, output, indent=4)

        print("[+] Results saved to: output.json")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        metavar="FILE",
        dest="file",
        help="File path for extraction",
    )
    args = parser.parse_args()

    extractor = IOCExtractor()
    extractor.extract_ioc(args.file)
