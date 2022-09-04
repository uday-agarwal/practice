import os
from configparser import ConfigParser

CONFIGURATION_FILE_PATH = 'config.ini'



def readConfig():
    config = ConfigParser()
    config.read(CONFIGURATION_FILE_PATH)
    return config

if __name__ == '__main__':
    os.chdir('.\LLD\serializer')    # If cwd is not the top directory where interpreter is running
    config = readConfig()
    print(config.sections())

    print(config['APP']['Name'])
    print(config['APP']['Version'])
    print(config['APP']['Enabled'])

    if config['APP']['Enabled']:
        print('enabled')
    else:
        print('disabled')

