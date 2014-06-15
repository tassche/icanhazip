from icanhazip import write_config
import configparser

def write_sample_config():
    config = configparser.ConfigParser()
    config['e-mail'] = {
        'from': 'from@example.org',
        'to': 'to@example.org',
        'subject': '[New IP] {ip}',
        'body': '{ip}',
        'smtp_server': 'smtp.example.org',
        'smtp_port': 25,
    }
    write_config(config)

if __name__ == '__main__':
    write_sample_config()
