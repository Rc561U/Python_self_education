#Generate two **CSV** report files and visualize data on the web.

First, import all the Python modules that you'll use in this Python script. After importing the necessary modules, initialize two dictionaries: one for the number of different error messages and another to count the number of entries for each user (splitting between INFO and ERROR).

Now, parse through each log entry in the syslog.log file by iterating over the file.

For each log entry, you'll have to first check if it matches the **INFO** or **ERROR** message formats. You should use regular expressions for this. When you get a successful match, add one to the corresponding value in the per_user dictionary. If you get an ERROR message, add one to the corresponding entry in the error dictionary by using proper data structure.

After you've processed the log entries from the **_syslog.log_** file, you need to sort both the per_user and error dictionary before creating **CSV** report files.





**csv_to_html.py** - converts the data in a CSV file into an HTML file that contains a table with the data.
**bash.sh** - bash command initialize and run scripts
**syslog.log** -main log file which contain all information about users
**ticky_check** - python script which return two _csv_ files
**error.log, info.log** - work result of bash.sh 
