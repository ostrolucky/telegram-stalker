#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A small bot printing online,offline statuses, as well as counts of messages they send to you
"""
from pytg.receiver import Receiver
from pytg.utils import coroutine
from dateutil.relativedelta import relativedelta
import datetime, colorama

@coroutine
def stalk(receiver):
    try:
        last = {}
        msg_counter = {}
        while True:
            msg = (yield)
            if msg['event'] == 'online-status':
                now = datetime.datetime.now()
                date = colorama.Style.DIM + now.strftime("%d.%b (%a) %H:%M:%S") + colorama.Style.RESET_ALL
                onlineStatus = (colorama.Fore.GREEN + 'online' if msg['online'] else colorama.Fore.RED + 'offline') + colorama.Fore.RESET
                userId = msg['user']['id']
                userName = msg['user']['print_name']
                nickName = colorama.Fore.YELLOW + userName + colorama.Fore.RESET
                lastChange = ''
                if last is not {} and userId in last:
                    diff = relativedelta(now, last[userId])
                    lastChange = ' [%02d:%02d:%02d]' % (diff.hours, diff.minutes, diff.seconds)
                    if not msg['online']:
                        lastChange = lastChange + ' (%d msgs)' % msg_counter.get(userId, 0)
                        msg_counter[userId] = 0
                last[userId] = now
                print(date + ': ' + nickName + ': ' + onlineStatus + lastChange)
            elif msg['event'] == 'message':
                userId = msg['sender']['id']
                msg_counter[userId] = msg_counter.get(userId, 0) + 1
    except KeyboardInterrupt:
        receiver.stop()
        print("Exiting")


if __name__ == '__main__':
    receiver = Receiver(port=4458)
    receiver.start()
    receiver.message(stalk(receiver))
receiver.stop()
