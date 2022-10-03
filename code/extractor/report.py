from datetime import datetime
from os.path import abspath, dirname

import urllib3
import yaml
from pymisp import MISPAttribute, MISPEvent, MISPOrganisation, MISPTag, PyMISP

urllib3.disable_warnings()


class ReportGenerator:
    def __init__(
        self,
        distribution: int = 1,
        info: str = "MISP Event",
        tags: list = ["tlp:amber"],
        analysis: int = 0,
        threat_level_id: int = 4,
        published: bool = False,
        orgc: str = "ORGNAME",
    ):
        self.distribution = distribution
        self.info = info
        self.tags = tags
        self.analysis = analysis
        self.threat_level_id = threat_level_id
        self.published = published
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.timestamp = datetime.now().timestamp()
        self.orgc = self.add_orgc(orgc)

    def generate_attribute(
        self, attr_type: str = None, value: str = None
    ) -> MISPAttribute:
        """Returns a MISPAttribute object."""
        attr = MISPAttribute()
        attr.value = value

        match attr_type:
            case "domain" | "email" | "url":
                attr.type = attr_type
            case "asn":
                attr.type = "as"
            case "cve":
                attr.type = "vulnerability"
            case "file_hash_md5":
                attr.type = "filename|md5"
            case "file_hash_sha1":
                attr.type = "filename|sha1"
            case "file_hash_sha256":
                attr.type = "filename|sha256"
            case "ipv4" | "ipv6":
                attr.type = "ip-src"
            case "mitre_att&ck":
                attr.type = "other"
            case "yara_rule":
                attr.type = "yara"
            case "mac_address":
                attr.type = "mac-address"
            case "file_name":
                attr.type = "filename"

        return attr

    def add_orgc(self, value: str = None) -> MISPOrganisation:
        """Returns a MISPOrganisation object."""
        orgc = MISPOrganisation()
        orgc.name = value
        return orgc

    def add_tag(self, value: str = None) -> MISPTag:
        """Returns a MISPTag object."""
        tag = MISPTag()
        tag.name = value
        return tag

    def generate_event(self, results: dict) -> (dict | MISPEvent):
        """Create MISPEvent object for later upload."""
        event = MISPEvent()
        event.info = self.info
        event.distribution = self.distribution
        event.analysis = self.analysis
        event.threat_level_id = self.threat_level_id
        event.date = self.date
        event.timestamp = self.timestamp
        event.published = self.published
        event.orgc = self.orgc

        if self.tags:
            for tag in self.tags:
                event.tags.append(self.add_tag(tag))

        for attr in results:
            if len(results[attr]) > 0:
                for value in results[attr]:
                    event.attributes.append(
                        self.generate_attribute(attr.lower(), value)
                    )

        return event

    def create_event(self, results: dict) -> None:
        """Create an event and upload it to MISP."""
        with open(dirname(dirname(abspath(__file__))) + "/config.yml") as f:
            config = yaml.safe_load(f)  # Load config file keys

        MISP_URL, MISP_KEY, MISP_VERIFYCERT = config["keys"].values()

        print("[+] Extracting document IOCs")

        misp = PyMISP(MISP_URL, MISP_KEY, MISP_VERIFYCERT)
        event = self.generate_event(results)
        print(f"[+] Event UUID: {event.uuid}")

        event = misp.add_event(event, pythonify=True)
        print(f"[+] Event successfully created with {len(event.attributes)} attributes")
