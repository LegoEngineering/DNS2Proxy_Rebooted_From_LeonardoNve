Task 2: Block Access to Certain Sites
____________________________________________________________________________________________________________________________________________________________________________
This folder includes:
modified .cfg
unmodified dns2proxy.py 
____________________________________________________________________________________________________________________________________________________________________________
The dns2proxy program already includes the ability to assign any particular IP to any specific domain name request by modifying the domains.cfg file. 
It was therefore unnecessary to modify the dns2proxy.py file for this task.
Each line of the .cfg document includes a domain name followed by the IP the user wishes to return in the event of that domain name request.
In order to block sites, the user assigns a local IP, like 192.168.127.127, to those domain names so their requests cannot span the internet.
All domain names are preceded by a period.

Included in this folder's .cfg ultimately blocks amazon.com and facebook.com
