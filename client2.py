#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from temperature import Temperature
from redis_settings import r

def task1():
    pubsub = r.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('temperature')
    
    while True:            
        for item in pubsub.listen():
            print item
        gevent.sleep(0)

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(task1)])
