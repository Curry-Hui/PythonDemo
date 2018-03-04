#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


def main():
    path = '/Users/huishuaishuai/hui/movies/java/javaSE/day16'
    i = 1
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            if '集合' in filename:
                print(filename)
                os.rename(os.path.join(path, filename), os.path.join(path, '0' + str(i) + filename[filename.find():]))
        i = i + 1


if __name__ == '__main__':
    main()
