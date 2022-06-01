#!/usr/bin/env bash
grep ' ERROR ' syslog.log > error.log
grep ' INFO ' syslog.log > info.log
sudo chmod +x csv_to_html.py
chmod +x ticky_check.py
./ticky_check.py
./csv_to_html.py user_statistics.csv /var/www/html/statistics.html
./csv_to_html.py error_message.csv /var/www/html/errors.html