#! /usr/env/python

import requests
import sys
import logging

IP = '192.168.188.22'
USER = '2TVMBPdD12TsazTaC474o1mEK5KZODZ8FEsAs199'
BASE_URL = f"http://{IP}/api/{USER}/"
format = '%(asctime)s : %(levelname)s : %(name)s.%(funcName)s : %(message)s'
logger = logging.getLogger()
formatter = logging.Formatter(format)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename='toggle.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def toggleLightByNumber(light):
    # Takes in light as integer to have state changed
    LIGHT_URL = f'lights/{light}/'
    get = requests.get(BASE_URL + LIGHT_URL)
    setstate = not get.json()['state']['on']
    setstate = str(setstate).lower()
    mydata = f'{{"on": {setstate}}}'
    logging.info('Changing Light State')
    put = requests.put(BASE_URL+LIGHT_URL+'state/', data=mydata)
    logging.debug(put.json())


def toggleGroupByNumber(group):
    # Takes in a group as an integer to have state changed
    GROUP_URL = f'groups/{group}/'
    get = requests.get(BASE_URL + GROUP_URL)
    setstate = not get.json()['action']['on']
    setstate = str(setstate).lower()
    mydata = f'{{"on": {setstate}}}'
    logging.info("Changing Group State")
    put = requests.put(BASE_URL + GROUP_URL + 'action/', data=mydata)
    logging.debug(put.json())
    toggleLightByNumber(1)
    counter = 5
    while True:
        counter -= 1
        get = requests.get(BASE_URL + GROUP_URL)
        all_on = get.json()['state']['all_on']
        any_on = get.json()['state']['any_on']
        if any_on == all_on:
            break
        else:
            logging.info("Changing Group State")
            put = requests.put(BASE_URL + GROUP_URL + 'action/', data=mydata)
            logging.debug(put.json())
            # toggleLightByNumber(1)
        if counter <= 0:
            logging.warning("Failed to flip state of all lights")
            sys.exit("FAILED TO FLIP STATE OF ALL LIGHTS!")


if __name__ == '__main__':
    logger.addHandler(stream_handler)
    toggleGroupByNumber(1)
