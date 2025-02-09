# TOOL-TO-MONITOR-CHANGES-IN-FILES-BY-CALCULATING-AND-COMPARING-HASH-VALUES

**COMPANY** : CODTECH IT SOLUTIONS

**NAME** : PRIYANSHU RAIKWAR

**INTERNID** : CT08LFM

**DOMAIN** : CYBER SECURITY AND ETHICAL HACKING

**BATCH DURATION** : JANUARARY 10TH , 2025 TO FEBRAUARY 10TH, 2025

**MENTOR NAME** : SRAVANI

**DESCRIPTION** : 
The File Integrity Checker Tool is a Python-based utility designed to monitor and ensure the integrity of files by calculating and comparing their hash values. This tool is essential for tracking changes in files, particularly in scenarios where file integrity is critical, such as configuration files, logs, or source code.

Key Features:

1.Hash Calculation: Utilizes MD5 hashing to detect modifications in files.

2.Notification System: Sends pop-up alerts for any detected file modifications.

3.Database Management: Maintains a local JSON database to store file paths, their corresponding hash values, and timestamps.

4.Continuous Monitoring: Periodically checks for file integrity and updates the database with new hash values.

5.Manual Operations: Provides an interactive command-line interface for adding/removing files and manually updating file hashes.

6.Usage Instructions:

#Add Files to Monitor:

Run file.py to add files to the monitoring database:

Command- file.py

#Verify

Run
Copy code
python file.py

Start Monitoring:

Execute int.py to begin monitoring files and receive alerts for any modifications:

Customization Options:

Adjust Monitoring Interval: Modify the time.sleep(30) in int.py to change the interval between scans.

Change Notification Gap: Alter the time.sleep(5) in int.py to adjust the delay between notifications.

Contributing: Feel free to fork this repository, open issues, or submit pull requests for improvements!
