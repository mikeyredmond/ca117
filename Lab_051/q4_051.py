#!/usr/bin/env python3

import sys

def stat(a):
   i = 0
   count = 0
   while i < len(a):
      count = count + a[i]
      i = i + 1

   mean = count / len(a)
   if len(a) % 2 == 1:
      median = a[len(a) // 2]
   else:
      median = (a[len(a) // 2] + a[(len(a) // 2) - 1]) / 2

   print('Mean:', '{:.1f}'.format(mean))
   print('Median:', '{:.1f}'.format(median))

def main():
   a = []
   for line in sys.stdin:
      l = line.strip()
      a.append(int(l))
   stat(sorted(a))

if __name__ == '__main__':
   main()
