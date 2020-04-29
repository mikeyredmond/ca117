#!/usr/bin/env python3

import sys

def mult(x):
   print("Multiples of 3:", [n for n in range(1, x + 1) if n % 3 == 0])
   print("Multiples of 3 squared:", [n ** 2 for n in range(1, x + 1) if n % 3 == 0])
   print("Multiples of 4 doubled:", [n * 2 for n in range(1, x + 1) if n % 4 == 0])
   print("Multiples of 3 or 4:", [n for n in range(1, x + 1) if n % 3 == 0 or n % 4 == 0])
   print("Multiples of 3 and 4:", [n for n in range(1, x + 1) if n % 3 == 0 and n % 4 == 0])
   print("Multiples of 3 replaced:", ["X" if not n % 3 else n for n in range(1, x + 1)])
   print("Primes:", [n for n in range(2, x + 1) if all(n % i != 0 for i in range(2, n))])

def main():
   x = int(sys.argv[1])
   mult(x)

if __name__ == '__main__':
   main()
