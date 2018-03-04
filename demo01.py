#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request
import requests
import re
import json


def get_stations():
    stations = dict()
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    response = requests.get(url, verify=False)
    pattern = re.compile('([A-Z]+)\|([a-z]+)')
    result = dict(re.findall(pattern, response.text))
    for key, value in result.items():
        stations[value] = key
        print(value)
    return stations


def get_station():
    stations = dict()
    # url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate=2017-10-05&from_station=CDW&to_station=SHH'
    # response = requests.get(url, verify=False)
    # print(response.json().decode('utf-8'))
    # print(response.json()['data'])
    # pattern = re.compile('([A-Z]+)\|([a-z]+)')
    # result = dict(re.findall(pattern, response.text))
    # for key, value in result.items():
    #     stations[value] = key
    # return stations
    response = urllib.request.urlopen('http://localhost/pool/hello.txt')
    with open('world.txt', 'wb') as f:
        f.write(response.read())

    with open('world.txt', 'r') as f:
        print(f.readlines()[0])


def main():
    # stations = get_stations()
    # for key in stations.keys():
    #     print(key)
    get_station()


if __name__ == '__main__':
    main()
