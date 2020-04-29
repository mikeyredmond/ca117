class PQ(object):

   def __init__(self):
      self.d = {}
      self.N = 0

   # Swap nodes i and j
   def exch(self, i, j):
      self.d[i], self.d[j] = self.d[j], self.d[i]

   # Add a new node to the heap
   def insert(self, v):
      self.N += 1
      self.d[self.N] = v
      self.swim(self.N)

   # Node k swims up the heap
   def swim(self, k):
      # while not at root and parent < child
      while k > 1 and self.d[k // 2] < self.d[k]:
         self.exch(k, k // 2)
         k = k // 2

   # Return the bigger of nodes i and j
   def bigger(self, i, j):
      try:
         return max([i, j], key=self.d.__getitem__)
      except KeyError:
         return i

   # Remove the max node
   def delMax(self):
      v = self.d[1]
      self.exch(1, self.N)
      del(self.d[self.N])
      self.N -= 1
      self.sink(1)
      return v

   # Node k sinks down the heap
   def sink(self, k):
      # While there is a left child
      while (2 * k <= self.N):
         # Index of left child
         j = 2 * k
         # Select bigger child
         j = self.bigger(j, j + 1)
         # Done if >= both children
         if self.d[k] >= self.d[j]:
            break
         # Swap with larger child
         self.exch(k, j)
         k = j

   # Return reference to max node
   def getMax(self):
      return self.d[1]

    # Is the heap empty
   def is_empty(self):
      return self.size() == 0

    # Size of heap
   def size(self):
      return self.N
