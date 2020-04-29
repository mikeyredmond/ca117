#!/usr/bin/env python3

import sys


def main():
   lines = sys.stdin.readlines()
   a = lines[0].strip().split()
   i = 0
   while i < len(a):
      a[i] = int(a[i])
      i += 1
   b = lines[1].strip().split()
   i = 0
   while i < len(b):
      b[i] = int(b[i])
      i += 1
   c = lines[2].strip().split()
   i = 0
   while i < len(c):
      c[i] = int(c[i])
      i += 1

   ab = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
   ac = ((c[0] - a[0]) ** 2 + (c[1] - a[1]) ** 2) ** 0.5
   if ac < ab:
      point = c
   elif ab == ac:
      point = a
   else:
      point = b
   pta = [a[0] - point[0], a[1] - point[1]]
   ptb = [b[0] - point[0], b[1] - point[1]]
   ptc = [c[0] - point[0], c[1] - point[1]]
   if pta != [0, 0] and ptc != [0, 0]:
      x = pta[0] + c[0]
      y = pta[1] + c[1]
   elif pta != [0, 0] and ptb != [0, 0]:
      x = pta[0] + b[0]
      y = pta[1] + b[1]
   elif ptb != [0, 0] and ptc != [0, 0]:
      x = ptb[0] + c[0]
      y = ptb[1] + c[1]

   print(x, y)

if __name__ == "__main__":
    main()
