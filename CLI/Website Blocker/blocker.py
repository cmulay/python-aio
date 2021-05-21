# imports
import time
from datetime import datetime as dt

# add websites to block
sites_to_block = ['www.1234.com', '1234.com']

# host locations
linux = '/etc/hosts'
macos = '/private/etc/hosts'
window = r"C:\Windows\System32\drivers\etc\hosts"

# select your host by replacing linux with yours
default_host = linux

redirect = "127.0.0.1"


# function for blocking
def blockers(start_time, end_time):
    while True:
        if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, end_time):
            print("Do the work ....")
            with open(default_host, 'r+') as hostfile:
                hosts = hostfile.read()
                for site in sites_to_block:
                    if site not in hosts:
                        hostfile.write(redirect + ' ' + site + '\n')
        else:
            with open(default_host, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print('Chill Bro !')
        time.sleep(3)


if __name__ == '__main__':
    '''
        Set working hour here
            (start_time, end_time)
    '''
    blockers(2, 3)
