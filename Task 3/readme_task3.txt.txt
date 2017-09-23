Task 3: Avoid Logging Blocked Sites
____________________________________________________________________________________________________________________________________________________________________________
This folder includes:
modified .cfg
modified dns2proxy.py (shown outside of the master folder for clarity)
unmodified dns2proxy folder without its domains.cfg or dns2proxy.py. 
____________________________________________________________________________________________________________________________________________________________________________
In order to avoid logging blocked sites, the program makes a list of strings from the .cfg file. The period is then omitted from each string.
The domain name request is then stored in a string. Blocking is set to zero.
The program looks to see if any of the members of the blocked sites array exist inside the domain name request. If they do, blocking is set to 1.
An if statement makes it so that logs are only recorded when blocking is zero.

Included in this folder's .cfg ultimately blocks amazon.com and facebook.com
