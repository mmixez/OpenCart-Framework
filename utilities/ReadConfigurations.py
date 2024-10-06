import configparser
from configparser import ConfigParser


def read_configuration(category,key):
    config = configparser.ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)