This is my first to add so bear with me to understand my logic.
I have 2 Raspberry PIs, 4 and a 5, both 8gb memory
Ras4 has the latest raspberry OS and Ras5 has ubuntu 24
I wanted both to email me the ip address on boot but making sure we have a connection and if now, we wait until we do
Used Cron with both OS using @reboot directpathto/bootfile.sh as an exsample
I used the bash script because in case I wanted to add python scripts to the file with out restarting or opening terminal.
As a side note, I also have a bash script running every min and even at 3am, so i can add python scripts as needed.

Some parts I coded and/or recoded plus copy and past from elsewhere.
This works great. Uses API from google to send emails to me.

Any updates to improve. let me know
