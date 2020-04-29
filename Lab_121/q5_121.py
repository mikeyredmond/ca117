#!/usr/bin/env python3

import sys

def sorter(t):
   return(t[1])

def main():
   d = {}
   for line in sys.stdin:
      line = line.strip().split(': ')
      nw = line[1].split(',')
      count = 0
      for score in nw:
         if score.isnumeric():
            count += int(score)
      avg = '{:.1f}'.format(count / 6)
      d[line[0]] = avg

   for (k, v) in sorted(d.items(), key=sorter, reverse=True):
      print('{}: {}'.format(k, v))


if __name__ == '__main__':
   main()
