#!/usr/bin/env python3

import sys
from priority_queue_112 import PQ

def main():
   cmdnum = int(sys.argv[1])
   pq = PQ()
   for num in sys.stdin:
      n = int(num.strip())

      if pq.size() < cmdnum:
         pq.insert(n)

      elif n < pq.getMax():
         pq.delMax()
         pq.insert(n)

   while not pq.is_empty():
      print(pq.delMax())

if __name__ == '__main__':
   main()
