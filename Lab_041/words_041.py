#!/usr/bin/env python3

import sys
import string


def main():
   a = []
   d = {}
   for line in sys.stdin:
      s = line.lower().strip().strip(string.punctuation).split()
      for l in s:
         s = a.append(l.strip(string.punctuation))
   x = sorted(a)
   for key in x:
      if key not in d:
         d[key] = x.count(key)
   for (k, v) in sorted(d.items()):
      print('{} : {}'.format(k, v))

if __name__ == '__main__':
   main()
