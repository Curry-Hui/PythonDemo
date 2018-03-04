#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from urllib import request
import json


def main():
    res = request.urlopen('https://www.baidu.com')
    # res = request.urlopen('http://www.dy2018.com/')
    data = res.read().decode('utf-8')
    print(type(json.loads(data)))


if __name__ == '__main__':
    main()