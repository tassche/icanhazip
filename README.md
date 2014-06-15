icanhazip.py
------------

Script that gets your IP address via [icanhazip.com][1] and sends it to you 
in an e-mail message.

It can be an alternative to a dynamic DNS provider if it is run at regular 
intervals, eg. using cron or Windows Task Scheduler.

The IP address is saved in the config file so that you would only receive an 
e-mail if the IP has changed since before.

[1]: http://icanhazip.com/


### Setup

Create the configuration file icanhazip.ini:

    $ python3 setup.py

Edit icanhazip.ini and specify your e-mail settings:

    [e-mail]
    from = you@your-isp.com
    to = you@gmail.com
    subject = [home] {ip}
    body = {ip}
    smtp_server = mail.your-isp.com
    smtp_port = 25
    

### Usage

    $ python3 icanhazip.py

Tested on Ubuntu 14.04 and Windows 8.1 using Python 3.4.

