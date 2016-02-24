#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def randomize():
    return round(random.uniform(20, 30), 2)

class Temperature(object):
    def __init__(self):
        pass

    def get_value(self):
        return randomize()
