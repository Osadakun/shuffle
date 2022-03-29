#!/usr/bin/env python
# coding: utf-8
import random

def shuffleDict(d):
  keys = list(d.keys())
  random.shuffle(keys)
  [(key, d[key]) for key in keys]
  random.shuffle(keys)
  [(key, d[key]) for key in keys]
  random.shuffle(keys)
  keys = [(key, d[key]) for key in keys]
  return dict(keys)

for k,v in shuffleDict(members).items():
  print("%7i%7s" %(k,v))