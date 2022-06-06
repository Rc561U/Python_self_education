# Fix a slow system with Python

## This is a qwiklabs of Week 2

You're an IT administrator for a media production company that uses Network-Attached Storage (NAS) to store all data generated daily (e.g., videos, photos). One of your daily tasks is to back up the data in the production NAS (mounted at /data/prod on the server) to the backup NAS (mounted at /data/prod_backup on the server). A former member of the team developed a Python script (full path /scripts/dailysync.py) that backs up data daily. But recently, there's been a lot of data generated and the script isn't catching up to the speed. As a result, the backup process now takes more than 20 hours to finish, which isn't efficient at all for a daily backup.