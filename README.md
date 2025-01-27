This is my first to add so bear with me to understand my logic.
I have 2 Raspberry PIs, 4 and a 5, both 8gb memory

I wanted to email myself the ip address on boot but making sure we have a connection and if not, we wait until we do
I also have it detect the distro and platform type and include this in the email.
I did this so once added, you should not have to edit anything and know what system the ip belongs to.

Used Cron adding @reboot directpathto/bootfile.py as an exsample

This works great. Uses API from google to send emails to me.

This can be used on any linux debian system. 

Any updates to improve. let me know
