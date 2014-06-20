icanhazip.py
------------

Script that gets your IP address via [icanhazip.com][1] and sends it to you 
in an email message.

It can be an alternative to a dynamic DNS provider if it is run at regular 
intervals, eg. using cron or Windows Task Scheduler.

The IP address is saved in the config file so that you would only receive an 
email if the IP has changed since before.

[1]: http://icanhazip.com/


### Setup

1. Save the files `icanhazip.py` and `icanhazip.ini` in the same directory, 
   eg. `/home/user/bin/icanhazip/`.
2. Edit `icanhazip.ini` and specify your email settings.


### Usage

    $ cd /home/user/bin/icanhazip
    $ python3 icanhazip.py

Tested on Ubuntu 14.04 and Windows 8.1 using Python 3.4.

