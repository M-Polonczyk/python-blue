import os
from log import log_writer
from datetime import datetime


def arp_table_extractor():
    arp_table = os.popen('arp -a').read()
    arp_table_lines = arp_table.splitlines()
    addresses = {'MAC': 'IP'}
    for line in arp_table_lines:
        if line.__contains__('ff:ff:ff:ff:ff:ff') or line.__contains__('ff-ff-ff-ff-ff-ff') or line.__contains__('Int'):
            continue
        if arp_table_lines.index(line) > 0:
            split_line = remove_items(line.split(' '), '')
            addresses[split_line[1]] = split_line[0]
    return addresses


def arp_table_mac_duplication(addr=[]):
    addr.sort()
    for i in range(len(addr) - 1):
        if addr[i] == addr[i + 1]:
            return addr[i]
    return False


addresses = arp_table_extractor()
mac_addr = []
for row in addresses.keys():
    mac_addr.append(row)
print(mac_addr)
duplicated = arp_table_mac_duplication(mac_addr)
# test
# duplicated = arp_table_mac_duplication(['01-5e-5e-01-00-fb', '01-01-5e-00-00-ff', '01-01-5e-00-00-ff']) 
log_writer(duplicated, datetime.now().strftime('%d/%m/%Y %H:%M:%S')) if duplicated is not False else print('All good!')
