from datetime import datetime

import yaml
from pymisp import MISPAttribute, MISPEvent, PyMISP


class ReportGenerator:
    def generate_attribute(self, attr_type: str = None, value: str = None) -> MISPAttribute:
        """Returns a MISPAttribute object."""
        attr = MISPAttribute()
        attr.value = value

        match attr_type:
            case 'domain' | 'email' | 'url':
                attr.type = attr_type
            case 'asn':
                attr.type = 'as'
            case 'cve':
                attr.type = 'vulnerability'
            case 'file_hash_md5':
                attr.type = 'filename|md5'
            case 'file_hash_sha1':
                attr.type = 'filename|sha1'
            case 'file_hash_sha256':
                attr.type = 'filename|sha256'
            case 'ipv4' | 'ipv6':
                attr.type = 'ip-src'
            case 'mitre_att&ck':
                attr.type = 'other'
            case 'yara_rule':
                attr.type = 'yara'
            case 'mac_address':
                attr.type = 'mac-address'
            case 'file_name':
                attr.type = 'filename'

        # print(f"[ATTRIBUTE] {attr}")
        return attr

    def generate_event(self, results: dict) -> (dict | MISPEvent):
        """Create MISPEvent object for later upload."""
        event = MISPEvent()
        event.add_tag('tlp:amber')
        event.analysis = 0
        event.threat_level_id = 3
        event.date = datetime.now().strftime('%Y-%m-%d')
        event.timestamp = datetime.now().timestamp()
        event.info = 'IOC Extractor Report'

        for attr in results:
            if len(results[attr]) > 0:
                for value in results[attr]:
                    event.attributes.append(self.generate_attribute(attr.lower(), value))
        
        return event

    def create_event(self, results: dict):
        # Load config file keys
        with open('keys.yml') as f:
            config = yaml.safe_load(f)

        MISP_KEY = config['keys']['misp_key']
        MISP_URL = config['keys']['misp_url']

        print("[+] Extracting document IOCs")

        misp = PyMISP(MISP_URL, MISP_KEY, 'json')
        event = self.generate_event(results)
        event = misp.add_event(event, pythonify=True)
