from pymisp import MISPAttribute, MISPEvent, PyMISP

MISP_URL = 'http://127.0.0.1/'
MISP_KEY = 'u7PoJuTNNcwLUzY6nn3Lqn6cXb3GnRVKNr0bZMXc'

def create_attribute(attr_type: str = None, value: str = None) -> MISPAttribute:
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

    print(f"[ATTRIBUTE] {attr}")

    return attr

results = {
    'status': 'success',
    'meta': {
        'len': 533, 'bytes': 533
    },
    'data': {
        'ASN': [],
        'CVE': [],
        'DOMAIN': [
            'vm-srv-1.gel.ulaval.ca', 'satkas.waw.pl'
        ],
        'EMAIL': [],
        'FILE_HASH_MD5': [],
        'FILE_HASH_SHA1': [],
        'FILE_HASH_SHA256': [
            '2a3b660e19b56dad92ba45dd164d300e9bd9c3b17736004878rf45ee23a0177ac', '1326932d63485e299ba8e03bfcd23057f7897c3ae0d26ed1235c4fb108adb105'
        ], 'IPv4': [
            '23.29.115.180', '156.96.46.116', '212.103.61.74', '23.82.128.144', '192.154.224.126', '188.34.185.85', '104.237.218.74'
        ],
        'IPv6': [],
        'MITRE_ATT&CK': [],
        'URL': [
            'http://satkas.waw.pl/rainloop/forecast'
        ],
        'YARA_RULE': [],
        'MAC_ADDRESS': [],
        'FILE_NAME': [
            'satkas.waw.pl'
        ]
    }
}
results = results['data']

event = MISPEvent()
misp = PyMISP(MISP_URL, MISP_KEY)

event.info = "Testing"

for attr in results:
    if len(results[attr]) > 0:
        for value in results[attr]:
            event.attributes.append(create_attribute(attr.lower(), value))

print(f"[ATTR_LIST] {event.attributes}")

event = misp.add_event(event, pythonify=True)
print(f"[EVENT] {event}")
