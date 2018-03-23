'''
Input data contain the number of commands in the first line.
The second line contains "commands" in form of integer values. Each positive value X mean "put the X to heap", while
0-s require you instead to extract the minimum from the heap (and forget of it).
Answer should contain the values in the array representing the heap after all commands are done.

Example:

input data:
13
3 9 6 5 7 1 11 2 0 10 4 8 0

answer:
3 4 6 5 7 8 11 10 9

To help you, let us trace how the heap is filled here:

At beginning, 3 is put to root, then 9 to its left and 6 to its right.

Next number 5 is at first placed as left child of 9 but then is swapped with it. Then 7 comes to right of 5:

                    3
                    |
             5------+------6
             |             |
         9---+---7      ---+---

After 1 is clinged to the left of 6 it pops to the top switching places with 6 and then with 3. Later 11 is placed at
the right of 3 with no more swaps.

Next element 2 is swapped with its parent 9 and grandparent 5, creating the following picture:

                    1
                    |
             2------+------3
             |             |
         5---+---7     6---+---11
         |
       9-+-

Then we meet 0 which tells us to delete the element from the heap. We remove the 1 and put the 9 from the bottom to its
place:

                    9
                    |
             2------+------3
             |             |
         5---+---7     6---+---11

But now the heap is broken and we need to exchange 9 with 2 and then with 5:

                    2
                    |
             5------+------3
             |             |
         9---+---7     6---+---11

We add 10 without swaps, then 4 exchanges places with 9 and 5, while 8 again makes no swaps:

                    2
                    |
             4------+------3
             |             |
         5---+---7     6---+---11
         |       |
      10-+-9   8-+

And the last command again asks us to remove the element - 2 goes away, 8 takes its place and is exchanged firstly
with 3 and then with 6:

                    3
                    |
             4------+------6
             |             |
         5---+---7     8---+---11
         |       |
      10-+-9     +

Resulting array could be "read" line by line from this picture:

3 4 6 5 7 8 11 10 9

Note that the the fact that, for example, 6 is to the right of the parent (3) and 4 to the left is just due to
coincidence. Unlike for binary tree the order of left and right children depends mainly on the order in which elements
are inserted rather on their relative values.
'''
from sys import stdin


class Binary_heap(object):
    def __init__(self):
        self.heap = []

    def __str__(self):
        return ' '.join([str(x) for x in self.heap])

    def put(self, elem):
        self.heap.append(elem)
        i = len(self.heap) - 1
        root = (i - 1) // 2
        while i > 0 and self.heap[root] >= self.heap[i]:
            self.heap[root], self.heap[i] = self.heap[i], self.heap[root]
            i, root = root, (root - 1) // 2

    def heapify(self, i):
        l, r, min = i * 2 + 1, i * 2 + 2, i
        if l < len(self.heap) and self.heap[l] < self.heap[min]:
            min = l
        if r < len(self.heap) and self.heap[r] < self.heap[min]:
            min = r
        if min != i:
            self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
            self.heapify(min)

    def pop(self):
        self.heap[0] = self.heap.pop()
        self.heapify(0)


def do_commands(array):
    bh = Binary_heap()
    for x in array:
        if x > 0:
            bh.put(x)
        else:
            bh.pop()
    return bh


print(*[do_commands(list(map(int, line.rstrip().split()))) for i, line in enumerate(stdin) if i > 0])
