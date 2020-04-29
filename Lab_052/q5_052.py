#!/usr/bin/env python3

import sys

def sorter(n):
   return n[1]

def mark(n):
   total = 0
   for num in n:
      total = total + int(num)
   return total

def main():
   d = {}
   a = []
   for line in sys.stdin:
      try:
         l = line.split(':')
         n = l[1].split(',')
         fn = l[0]
         d[fn] = mark(n)
      except ValueError:
         a.append(fn)
         continue

   for (k, v) in sorted(d.items(), key=sorter, reverse=True):
      print('{} : {}'.format(k, v))
   if len(a) >= 1:
      print('Skipped:')
      for name in a:
         print(name)

if __name__ == '__main__':
   main()
