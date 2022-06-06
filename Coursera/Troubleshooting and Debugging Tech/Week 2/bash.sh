#!/usr/bin/env bash

sudo apt install python3-pip
pip3 install psutil
sudo chmod +x ~/scripts/multisync.py
./scripts/multisync.py
sudo chmod +x ~/scripts/dailysync.py
./scripts/dailysync.py