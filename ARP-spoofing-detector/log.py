

def log_writer(mac_address, date):
    with open('log.txt', 'a') as f:
        f.write('Arp Spoofed!\n')
        f.write('The address is: ')
        f.write(mac_address)
        f.write('\nDate: ')
        f.write(date)
        f.write('\n')



log_writer('aa-aa-aa-aa-aa-aa','123456')