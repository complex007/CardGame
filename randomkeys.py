#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import json
import random
f=open('card_map.json')
d = json.load(f)
keylist=d.keys()
random.shuffle(keylist)
print keylist