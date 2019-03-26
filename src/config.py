import configparser
import os

global_config = configparser.ConfigParser()
global_config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')
config = global_config[global_config['DEFAULT']['CURRENT_CONFIG']]


