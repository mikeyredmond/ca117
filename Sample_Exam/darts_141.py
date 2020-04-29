#!/usr/bin/env python3

import sys

def main():
   count = 0
   for line in sys.stdin:
      line = line.strip().split()
      x = int(line[0])
      y = int(line[1])
      distance = ((x - 0) ** 2 + (y - 0) ** 2) ** 0.5
      if distance <= 20:
         count += 10
      elif distance <= 40:
         count += 9
      elif distance <= 60:
         count += 8
      elif distance <= 80:
         count += 7
      elif distance <= 100:
         count += 6
      elif distance <= 120:
         count += 5
      elif distance <= 140:
         count += 4
      elif distance <= 160:
         count += 3
      elif distance <= 180:
         count += 2
      elif distance <= 200:
         count += 1
      elif distance > 200:
         count += 0
   print(count)


if __name__ == '__main__':
   main()
