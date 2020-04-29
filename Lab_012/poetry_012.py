#!/usr/bin/env python3

import sys

b = []
def main():
   n = 0
   for line in sys.stdin:
      if n < len(line):
         n = len(line)
      b.append(line.strip())
   t = "{:^" + str(n - 1) + "s}"
   for p in b:
      print(t.format(p))


if __name__ == '__main__':
   main()
