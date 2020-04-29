#!/usr/bin/env python3

import sys

bn = {
   "2": "twenty",
   "3": "thirty",
   "4": "forty",
   "5": "fifty",
   "6": "sixty",
   "7": "seventy",
   "8": "eighty",
   "9": "ninety",
   "20": "twenty",
   "30": "thirty",
   "40": "forty",
   "50": "fifty",
   "60": "sixty",
   "70": "seventy",
   "80": "eighty",
   "90": "ninety",
   "100": "one hundred",
}

d = {
   "0": "zero",
   "1": "one",
   "2": "two",
   "3": "three",
   "4": "four",
   "5": "five",
   "6": "six",
   "7": "seven",
   "8": "eight",
   "9": "nine",
   "10": "ten",
   "11": "eleven",
   "12": "twelve",
   "13": "thirteen",
   "14": "fourteen",
   "15": "fifteen",
   "16": "sixteen",
   "17": "seventeen",
   "18": "eighteen",
   "19": "nineteen",
}

def main():
   for line in sys.stdin:
      a = ""
      s = line.strip().split()
      for number in s:
         if number in d:
            a = a + d[number] + " "
         elif number in bn:
            a = a + bn[number] + " "
         elif number not in d or bn:
            a = a + bn[number[0]] + "-" + d[number[1]] + " "
      print(a[:-1])

if __name__ == '__main__':
   main()
