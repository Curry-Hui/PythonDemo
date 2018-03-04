#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from qqbot import _bot as bot
import random


def main():
    bot.Login(['-q', '1412346295'])
    friends = bot.List('buddy')
    # friends = bot.List('buddy', '')
    friends = random.sample(friends, 100)
    for friend in friends:
        # print(friend)
        bot.SendTo(friend, 'Hello %s, 这是程序测试随机发送的信息，如您收到请忽略。' % friend)


if __name__ == '__main__':
    main()
