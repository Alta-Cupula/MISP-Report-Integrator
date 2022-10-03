import requests
from bs4 import BeautifulSoup


class URLFetch:
    @staticmethod
    def fetch(url: str) -> str:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html5lib")
            content = soup.get_text()
        except:
            content = ""

        return content
