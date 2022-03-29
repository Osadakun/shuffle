#!/usr/bin/env python
# coding: utf-8
import random
members = {1915053:"小野紀輝", 1916984:"鈴木智紀", 1102646:"池田了哉", 1901805:"北川裕基", 1139952:"中屋飛人", 1914801:"笹野章彦", 1102691:"石原泰知", 1140347:"近川健太"}

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