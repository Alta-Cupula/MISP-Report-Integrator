#!/usr/bin/env python
# -*- coding: utf-8 -*-

from extractor import IOCExtractor, ReportGenerator


def main():
    # Extracting IOCs
    extractor = IOCExtractor()
    results = extractor.extract_ioc(args.file, args.url)

    # Generating report
    report = ReportGenerator(
        args.distribution,
        args.info,
        args.tag,
        args.analysis,
        args.threat,
        args.published,
        args.orgc,
    )
    report.create_event(results)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        metavar="FILE",
        dest="file",
        default=None,
        help="File path for extraction",
    )
    parser.add_argument(
        "-u",
        "--url",
        required=False,
        metavar="URL",
        dest="url",
        default=None,
        help="URL for IOC extraction",
    )
    parser.add_argument(
        "--distribution",
        required=False,
        metavar="ID",
        dest="distribution",
        help="Set which groups have access to this event; Choose between 0 (Your organization only), 1 (This community only), 2 (Connected communities), 3 (All communities), 4 (Sharing group) and 5 (Inherit Event)",
    )
    parser.add_argument(
        "--info",
        required=False,
        metavar="INFO",
        default="MISP Event",
        dest="info",
        help="Information about the MISP event",
    )
    parser.add_argument(
        "--orgc",
        required=False,
        dest="orgc",
        default="ORGNAME",
        metavar="ORGANISATION",
        help="Set a custom creator organisation",
    )
    parser.add_argument(
        "--tag",
        required=False,
        metavar="TAG",
        dest="tag",
        nargs="+",
        default=["tlp:amber"],
        help="Tags to be added to MISP event separeted by space; i.e. tlp:amber tlp:white",
    )
    parser.add_argument(
        "--analysis",
        required=False,
        metavar="ID",
        dest="analysis",
        type=int,
        help="Current status of event analysis; Choose between 0 (Initial), 1 (Ongoing) and 2 (Complete)",
    )
    parser.add_argument(
        "--threat-level",
        required=False,
        metavar="ID",
        dest="threat",
        help="Threat level ID; Choose between 1 (High), 2 (Medium), 3 (Low) and 4 (Undefined)",
    )
    parser.add_argument(
        "--published",
        required=False,
        dest="published",
        default=False,
        action="store_true",
        help="Set event published value to True",
    )
    args = parser.parse_args()

    if not args.file and not args.url:
        exit(f"[!] Missing filename or URL")
    elif args.file and args.url:
        exit(f"[!] Please choose between a URL or filename")
    else:
        main()
