"""heap operations：insert"""
def _swap(self, i, j):
    self._pq[i], self._pq[j] = self._pq[j], self._pq[i]  # swap two elements in the list

def _less(self, i, j):
    return self._pq[i] < self._pq[j]

def _swim(self, k):
    while k > 1 and self._less(k//2, k):
        self._swap(k//2, k)
        k //= 2

def insert(self, key):
    self._pq.append(key)
    self._swim(self.size())

    '''heap operations：delete max'''
def _sink(self, k):
    while 2 * k <= self.size():
        j = 2 * k
        if j < self.size() and self._less(j, j + 1):
            j += 1  # after swapping, root is the smaller one,choose the larger child to sink
        if not self._less(k, j):
            break  # heap property satisfied, exit loop
        self._swap(k, j)
        k = j
def del_max(self):
    if self.is_empty():
        raise NoElement
    root = self._pq[1]
    self._swap(1, self.size())
    self._pq.pop()
    self._sink(1)
    return root
'''heap construction:A max binary heap'''
class MaxPQ:
    def __init__(self, data=None):
        self._pq = []
        self._pq.append(None)  # append a dummy key at index 0,so that element index starts from 1
        if data is not None:
            self._pq.extend(data)
            n = len(data)
            for k in range(n // 2, 0, -1): #starting from n//2 down to 1
                self._sink(k)