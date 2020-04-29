#!/usr/bin/env python3

import sys
import string


def main():
   a = []
   d = {}
   for line in sys.stdin:
      s = line.lower().lstrip().strip().strip(string.punctuation).split()
      for word in s:
         s = a.append(word.strip(string.punctuation))
   x = sorted(a)
   for key in x:
      if key not in d and len(key) > 3 and x.count(key) >= 3:
         d[key] = x.count(key)
   for (k, v) in sorted(d.items()):
      print('{:>{:d}s} : {:{:d}d}'.format(k, 9, v, 2))

if __name__ == '__main__':
   main()
