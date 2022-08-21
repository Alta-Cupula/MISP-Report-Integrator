#!/usr/bin/env python
# -*- coding: utf-8 -*-

from extractor import IOCExtractor, ReportGenerator


def main():
    # Extracting IOCs from PDF
    extractor = IOCExtractor()
    results = extractor.extract_ioc(args.file)
    
    print("[+] Extracted successfully")

    # Generating report
    report = ReportGenerator()
    report.create_event(results)

    print("[+] Uploaded successfully")

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

    main()

