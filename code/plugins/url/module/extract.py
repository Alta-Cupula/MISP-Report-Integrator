import re

from pymisp import MISPAttribute


class Extractor:
    def generate_attribute(self, attr_type: str = None, value: str = None) -> MISPAttribute:
        """Returns a MISPAttribute object."""
        attr = MISPAttribute()
        attr.type = attr_type
        attr.value = value

        return attr

    def hash_finder(self, content: str) -> list:
        pattern = re.compile("[0-9a-zA-Z]{30,}")
        match = pattern.findall(content)
        return match

    def ip_finder(self, content: str) -> list:
        pattern = re.compile("(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)")
        match = pattern.findall(content)
        addrs = ['.'.join(x) for x in match]
        return ["ip-src"]

    def extract_ioc(self, content: str) -> list:
        return self.ip_finder(content)


import requests

request = requests.get('https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/')
x = Extractor()
print(x.extract_ioc(request.text))
