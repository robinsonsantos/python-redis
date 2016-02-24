#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gevent
from temperature import Temperature
from redis_settings import r

def task1():
    count = 0
    while True:            
        t = Temperature()
        _t = t.get_value()

        r.publish('temperature', _t)
        count += 1

        print 'count: ', count
        print 'temperature: ', _t 
        gevent.sleep(0)

if __name__ == '__main__':
    gevent.joinall([gevent.spawn(task1)])
