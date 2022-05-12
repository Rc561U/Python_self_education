import os
import shutil
import sys

def check_reboot():
    '''Returns True if the computer has a pending reboot'''
    return os.path.exists('/run/reboot-required')

def check_disk_full(disk, min_gb, min_percent):
    '''Returns True if there isn't enough disk space, False otherwise.'''
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2 **30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False

def check_root_full():
    '''Returns True is root partition is full, False otherwise'''
    return check_disk_full(disk='/', min_gb=2, min_percent=10)

def main():
    everything_ok = True
    checks = [
            (check_reboot, 'Pendig Reboot'),
            (check_root_full, 'Root partition full'),
    ]

    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
        sys.exit(1)

    print('Everything ok. Your disk space is optimal ( compare with 2GB and 10% )')
    sys.exit(0)

main()