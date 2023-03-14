import os
from log import log_writer
import datetime
import ipaddress


def arp_table_extractor():
    arp_table = os.popen('arp -a').read()
    arp_table_lines = arp_table.splitlines()
    addresses = {}
    i = 0
    for line in arp_table_lines:
        if line.__contains__('ff:ff:ff:ff:ff:ff') or line.__contains__('ff-ff-ff-ff-ff-ff'):
            continue
        elif i > 2:
            split_line = line.split(' ')
            for j in range(len(split_line)):
                split_line.sort()
                if split_line[0] == '':
                    split_line.remove('')
                else:
                    break
            addresses[split_line[0]] = split_line[1]
        i += 1

    print(addresses.keys())
    print(addresses.values())
    print(arp_table_lines)
    return addresses


def arp_table_mac_duplication(addr=[]):
    addr.sort()
    for i in range(0, len(addr) - 1):
        if addr[i] == addr[i + 1]:
            return i
    return False


addresses = arp_table_extractor()
mac_addr = []
for row in addresses.keys():
    mac_addr.append(row)
print(mac_addr)
index = arp_table_mac_duplication(mac_addr)
if index == type(int):
    log_writer(mac_addr[index], datetime)
