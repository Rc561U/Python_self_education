import os
import shutil
import socket
import sys

def checkDiskSpace():
    '''Returns True if the computer has a pending reboot'''
    return os.path.exists('/run/reboot-required')

def checkDiskFull(disk, min_gb, min_percent):
    '''Returns True if there isn't enough disk space, False otherwise.'''
    du = shutil.disk_usage(disk)
    #calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2 **30
    if gigabytes_free <= min_gb or percent_free <= min_percent:
        return True
    return False

def checkRootFull():
    '''Returns True if root partition is full, False otherwise'''
    return checkDiskFull(disk='/', min_gb=2, min_percent=10)

def checkNoNetwork():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
        socket.gethostbyname('www.google.com')
        return False
    except:
        return True
def main():
    outputResult = True
    checks = [
        (checkDiskSpace, 'Pendig Reboot'),
        (checkRootFull, 'Root partition full'),
        (checkNoNetwork, 'No working network'),
    ]

    for check, msg in checks:
        if check():
            print(msg)
            outputResult = False

    if not outputResult:
        sys.exit(1)

    print('Test successfully completed.\nYour disk root space is in optimal condition (default values is 2GB and 10%)')
    sys.exit(0)

main()
