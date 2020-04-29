#!/usr/bin/env python3

import sys
import datetime

def main():
   for line in sys.stdin:
      a = line.strip().split()
      newtime = datetime.datetime.strptime(a[0], "%H:%M")
      newtime -= datetime.timedelta(minutes=int(a[1]))
      print(str(newtime.time())[0:5])

if __name__ == '__main__':
   main()
