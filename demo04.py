#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itchat
import json


def main():
    name_list = []
    itchat.auto_login(True)
    # f = itchat.search_friends(name='朱琳')
    # print(f)
    friends = itchat.get_friends()
    print(len(friends))
    for friend in friends:
        # print(str(friend))
        f = str(friend)
        flist = f.split(',')
        for l in flist:
            if 'RemarkName' in l:
                d = l[l.find(':') + 3:-1]
                if d:
                    name_list.append(d)
                    continue
            if 'NickName' in l:
                name_list.append(l[l.find(':') + 3:-1])
    print(len(name_list))
    for n in name_list:
        print(n)


if __name__ == '__main__':
    main()
