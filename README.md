# MISP Report Integrator

During my Bachelor's degree course I was able to compete in a challenge with my colleagues for a money prize of R$5000,00. The main objective was to developed a solution to a given problem while showing our skills. Together with my team I was able to win this prize and this is the final code.  

As proposed by the FIAP's Cybersecurity Challenge, the tool aims to perform the collection of Indicators of Compromise (IOCs) and generate a report that will later be added to the MISP platform, thus requiring the MISP API integration. For easy understanding and development of the code, the choosen programming language was Python. 

## Features

- Supports DOCX, PDF and URLs
- VirusTotal API integration for IOCs validation
- MalwareBazaar API integration for IOCs validation
- MISP API integration
- Multiple file extension outputs

## Resources Used
- Docker MISP Installation: [Github](https://github.com/misp/misp-docker)
- Crowdstrike IOC Samples: [Crowdstrike](https://www.crowdstrike.com/blog/observations-from-the-stellarparticle-campaign/)
- Python PyMISP API: [PyPi](https://pypi.org/project/pymisp/)
- MISP Official API: [Misp Project](https://www.misp-project.org/openapi/)
- STIX/TAXII Guide on Internal Resource Sharing: [Anomali](https://www.anomali.com/pt/resources/what-are-stix-taxii)
