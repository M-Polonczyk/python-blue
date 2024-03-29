import os
from typing import Dict, List
from log import log_writer
from datetime import datetime


def arp_table_extractor() -> Dict[str, str]:
    arp_table = os.popen("arp -a").read()
    arp_table_lines = arp_table.splitlines()
    addresses = {"IP": "MAC"}
    for line in arp_table_lines:
        if "ff:ff:ff:ff:ff:ff" in line or "ff-ff-ff-ff-ff-ff" in line or "Int" in line:
            continue
        if arp_table_lines.index(line) > 0:
            split_line = line.split(" ")
            addresses[split_line[0]] = split_line[1]
    return addresses


def arp_table_mac_duplication(addr: List[str]):
    addr.sort()
    for i in range(len(addr) - 1):
        if addr[i] == addr[i + 1]:
            return addr[i]
    return False


addresses = arp_table_extractor()
duplicated = arp_table_mac_duplication([row for row in addresses.values()])
# test
# duplicated = arp_table_mac_duplication(['01-5e-5e-01-00-fb', '01-01-5e-00-00-ff', '01-01-5e-00-00-ff'])
log_writer(
    duplicated, datetime.now().strftime("%d/%m/%Y %H:%M:%S")
) if duplicated is not False else print("All good!")
