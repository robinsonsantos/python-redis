#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import gevent
from temperature import Temperature

def task1():
    count = 0
    r = redis.Redis(host='localhost', port=6379, db=0)
    while True:            
        t = Temperature()
        _t = t.get_value()

        r.set('temperature', _t)
        count += 1

        print 'count: ', count
        print 'temperature: ', _t 
        gevent.sleep(0)

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(task1)])
