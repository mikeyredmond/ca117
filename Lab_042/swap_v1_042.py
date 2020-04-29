#!/usr/bin/env python3

import sys

def swap_keys_values(d):
   d1 = {}
   for key in d:
      d1[d[key]] = key

   return d1
