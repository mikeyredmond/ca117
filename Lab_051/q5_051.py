#!/usr/bin/env python3

import sys

def sorter(t):
   return sec(t[-1])

def sec(t):
   [m, s] = t.split(':')
   total = int(m) * 60 + int(s)
   return total

def main():
   d = {}
   for line in sys.stdin:
      try:
         s = line.strip().split()
         name, times = s[0], s[1:]
         d[name] = min(times, key=sec)
      except ValueError:
         continue

   wname, wtime = min(d.items(), key=sorter)
   print('{} : {}'.format(wname, wtime))

if __name__ == '__main__':
   main()
