#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ====================================================================================================
#
#         FILE : config_operations.py
#      CREATED : 07-nov.-2019
#         DESC : Create, Read, Update, Delete config files with configparser (built-in module)
#        USAGE : ./config_operations.py
# ====================================================================================================

import os, configparser


def createConfig(path, sections, settings):
    """
    Create a config file
    # - sections = List of sections ex: ['Setting', 'Variables']
    # - settings = Dict of tuples ex: {'section': {key: value, key: value}, 'section2': {key: value}}
    """
    config = configparser.ConfigParser()
    for section in sections:
        config.add_section(section)

    for section, values in settings.items():
        for option, value in values.items():
            try:
                config.set(section, option, value)
            except Exception as err:
                print(err)

    with open(path, 'w') as config_file:
        config.write(config_file)
    print('Done Creating Config File: {}'.format(path))


def getConfig(path):
    '''Returns the config object'''
    if not os.path.exists(path):
        createConfig(path)
    config = configparser.ConfigParser()
    config.read(path)
    return config


def getSettings(path, section, setting):
    '''Print out a setting'''
    config = getConfig(path)
    value = config.get(section, setting)
    msg = '{} {} is {}'.format(section, setting, value)
    print(msg)
    return value


def updateSetting(path, section, setting, value):
    '''Update a setting'''
    config = getConfig(path)
    config.set(section, setting, value)
    with open(path, 'w') as config_file:
        config.write(config_file)


def deleteSetting(path, section, setting):
    ''' Delete a setiing '''
    config = getConfig(path)
    config.remove_option(section, setting)
    with open(path, 'w') as config_file:
        config.write(config_file)


if __name__ == '__main__':
    path = '../laboratory/settings.ini'
    settings = {'Settings': {'font': 'Monaco', 'font_size': '12', 'font_style': 'Normal'},
                'Global Variables': {'PATH': '/var/log', 'USER': 'Dabve'}}
    createConfig(path, list(settings.keys()), settings)

    # font = getSettings(path, 'Settings', 'font')
    # font_size = getSettings(path, 'Settings', 'font_size')
    # updateSetting(path, 'Settings', 'font_size', '12')
    # deleteSetting(path, 'Settings', 'font_style')
