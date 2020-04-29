from stack_092 import Stack

def normal(op, p1, p2):
   if op == "+":
      return p1 + p2
   elif op == "-":
      return p2 - p1
   elif op == "*":
      return p1 * p2
   elif op == "/":
      return p2 / p1

def special(op, p):
   if op == "n":
      return -p
   elif op == "r":
      return p ** 0.5

def calculator(line):
   s = Stack()
   normalop = ["+", "-", "*", "/"]
   specialop = ["r", "n"]
   l = line.split()
   for char in l:
      if char not in normalop and char not in specialop:
         s.push(char)
      elif char in normalop:
         p1 = float(s.pop())
         p2 = float(s.pop())
         s.push(normal(char, p1, p2))
      elif char in specialop:
         p = float(s.pop())
         s.push(special(char, p))
   return float(s.top())
