#!/usr/bin/env python3

import sys

count = [0] * 10

def poker(s):
   count[s] += 1


def main():
   lines = sys.stdin.readlines()
   length = len(lines)
   for l in lines:
      l = l.rstrip()
      poker(int(l[-1]))

   print("The probability of nothing is {:.4f}%".format(count[0] / length * 100))
   print("The probability of one pair is {:.4f}%".format(count[1] / length * 100))
   print("The probability of two pairs is {:.4f}%".format(count[2] / length * 100))
   print("The probability of three of a kind is {:.4f}%".format(count[3] / length * 100))
   print("The probability of a straight is {:.4f}%".format(count[4] / length * 100))
   print("The probability of a flush is {:.4f}%".format(count[5] / length * 100))
   print("The probability of a full house is {:.4f}%".format(count[6] / length * 100))
   print("The probability of four of a kind is {:.4f}%".format(count[7] / length * 100))
   print("The probability of a straight flush is {:.4f}%".format(count[8] / length * 100))
   print("The probability of a royal flush is {:.4f}%".format(count[9] / length * 100))

if __name__ == '__main__':
   main()
