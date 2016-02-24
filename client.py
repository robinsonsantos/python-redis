#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import gevent
from temperature import Temperature

def task1():
    r = redis.Redis('localhost', port=6379, db=0)
    while True:            
        print r.get('temperature')
        gevent.sleep(0)

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(task1)])
