#!/usr/bin/env python3

import sys

def main():
   a = []
   for line in sys.stdin:
     line = line.strip()
     a.append(line)
   if len(a) % 2 == 0 and len(a) != 4:
      i = 2
      while i < len(a):
         tmp = a[i]
         a[i] = a[i - 1]
         a[i - 1] = tmp
         i += 1
      t = 2
      while t + 1 < len(a) - 1:
            tmp = a[t + 1]
            a[t + 1] = a[t]
            a[t] = tmp
            t += 1
      for word in a:
         print(word)

   elif len(a) % 2 == 1 and len(a) != 1:
      i = 2
      while i < len(a):
         tmp = a[i]
         a[i] = a[i - 1]
         a[i - 1] = tmp
         i += 1
      tmp = a[-2]
      a[-2] = a[2]
      a[2] = tmp
      for word in a:
         print(word)

   elif len(a) == 1:
      print(a[0])

   elif len(a) == 4:
      tmp = a[3]
      a[3] = a[2]
      a[2] = tmp
      for word in a:
         print(word)

if __name__ == '__main__':
   main()
