import sys
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.heap = []
        self.size = 0

    def push(self, x):
        self.heap.append(x)
        self.size += 1
        self.up_heapify(self.size-1)

    def pop(self):
        if self.size == 0:
            return 0
        else:
            self.swap(0, self.size-1)
            self.size -= 1
            self.down_heapify(0)
            return self.heap.pop()

    def up_heapify(self, index):
        if index == 0:
            return
        parent_index = (index-1)//2
        if self.heap[parent_index] < self.heap[index]:
            self.swap(parent_index, index)
            self.up_heapify(parent_index)
        else:
            return

    def down_heapify(self, index):
        left_index = index*2+1
        right_index = index*2+2
        if left_index >= self.size:
            return
        elif right_index >= self.size:
            if self.heap[left_index] > self.heap[index]:
                self.swap(left_index, index)
                self.down_heapify(left_index)
            else:
                return
        else:
            if self.heap[left_index] > self.heap[right_index]:
                if self.heap[left_index] > self.heap[index]:
                    self.swap(left_index, index)
                    self.down_heapify(left_index)
                else:
                    return
            else:
                if self.heap[right_index] > self.heap[index]:
                    self.swap(right_index, index)
                    self.down_heapify(right_index)
                else:
                    return

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

max_heap = Heap()
min_heap = Heap()

t = int(input())
for _ in range(t):
    k = int(input())
    for __ in range(k):
        func, num = input().rstrip().split()
        num = int(num)
        if func == 'I':
            max_heap.push(-num)
            min_heap.push(num)
        else:
            if num == 1:
                if max_heap.heap:
                    max_heap.pop()
                    min_heap.heap = min_heap.heap[:-1]
            else:
                if max_heap.heap:
                    max_heap.heap = max_heap.heap[:-1]
                    min_heap.pop()

print(min_heap)
print(max_heap)
