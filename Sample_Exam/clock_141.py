#!/usr/bin/env python3

import sys

def main():
   both_times = []
   for line in sys.stdin:
      line = line.strip()
      both_times.append(line)
   a = int(both_times[0])
   b = int(both_times[1])
   if b - a < a + (b - a):
      print(b - a)
   elif (b - a) == -(a - b):
      print(b - a)

if __name__ == '__main__':
   main()
