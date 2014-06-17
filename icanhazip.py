from email.mime.text import MIMEText
from smtplib import SMTP
import configparser
import urllib.request

config_file = 'icanhazip.ini'

def get_ip_address():
    request = urllib.request.Request('http://icanhazip.com')
    with urllib.request.urlopen(request) as response:
        ip_addr = str(response.read(), 'utf-8')
    return ip_addr.replace('\n', '')

def send_email(from_addr, to_addr, subject, body, server, port):
    message = MIMEText(body)
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = subject
    with SMTP(server, port) as smtp:
        smtp.send_message(message)

def read_config():
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def write_config(config):
    with open(config_file, 'w') as ini:
        config.write(ini)

if __name__ == '__main__':
    config = read_config()

    try:
        current_ip_addr = config['icanhazip']['ip_addr']
    except KeyError:
        config['icanhazip'] = {'ip_addr': ''}
        write_config(config)
        current_ip_addr = None

    ip_addr = get_ip_address()

    if ip_addr != current_ip_addr:
        email = config['e-mail']
        subject = email['subject'].format(ip=ip_addr)
        body = email['body'].format(ip=ip_addr)
        send_email(email['from'], email['to'], subject, body, 
                   email['smtp_server'], email['smtp_port'])

        config['icanhazip']['ip_addr'] = ip_addr
        write_config(config)

