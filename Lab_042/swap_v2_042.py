#!/usr/bin/env python3

import sys

def swap_unique_keys_values(d):
   d1 = {}
   for key in d:
      if d[key] not in d1:
         d1[d[key]] = key
      else:
         d1.pop(d[key])

   return d1
