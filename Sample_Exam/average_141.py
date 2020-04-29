#!/usr/bin/env python3

import sys

def main():
   count = 0
   words = []
   for line in sys.stdin:
      line = line.strip()
      words.append(line)
      count += len(line)
   average = count / len(words)
   print('Average: {:.2f}'.format(average))
   for word in words:
      if len(word) > average:
         print(word)

if __name__ == '__main__':
   main()
