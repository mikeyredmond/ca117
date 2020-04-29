#!/usr/bin/env python3

import sys

def l2d(s):
   s = sys.stdin.readline().strip().split()
   p = sys.stdin.readline().strip().split()
   d = {}
   i = 0
   while i < len(s):
      d[s[i]] = p[i]
      i += 1

   return d
