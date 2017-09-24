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
                userName = msg['user']['print_name']
                nickName = colorama.Fore.YELLOW + userName + colorama.Fore.RESET
                lastChange = ''
                if last is not {} and userName in last:
                    diff = relativedelta(now, last[userName])
                    lastChange = ' [%02d:%02d:%02d]' % (diff.hours, diff.minutes, diff.seconds)
                    if not msg['online']:
                        lastChange = lastChange + ' (%d msgs)' % (msg_counter[userName] if userName in msg_counter else 0)
                        msg_counter[userName] = 0
                last[userName] = now
                print(date + ': ' + nickName + ': ' + onlineStatus + lastChange)
            elif msg['event'] == 'message':
                msg_counter[msg['user']['print_name']] = msg_counter[userName] + 1 if userName in msg_counter[userName] else 1
    except KeyboardInterrupt:
        receiver.stop()
        print("Exiting")


if __name__ == '__main__':
    receiver = Receiver(port=4458)
    receiver.start()
    receiver.message(stalk(receiver))
receiver.stop()
