This is my first to add so bear with me to understand my logic.
I have 2 Raspberry PIs, 4 and a 5, both 8gb memory

I wanted to email myself the ip address on boot but making sure we have a connection and if now, we wait until we do
I also have it detect the distro and platform type and include this in the email.
I did this so once added, you should not have to edit anything and know what system the ip belongs to.

Used Cron with both OS using @reboot directpathto/bootfile.py as an exsample

Some parts I coded and/or recoded plus copy and past from elsewhere.
This works great. Uses API from google to send emails to me.

This can be used on any linux debian system as well. 

Any updates to improve. let me know
