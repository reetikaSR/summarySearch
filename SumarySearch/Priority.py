from queue import PriorityQueue


class PriorityQ:
    '''
    A wrapper class over priority heap for our usecase, to maintain the top k elements and discard the smaller elemensts
    and finally get the remaining elements in reverse sorted order.
    '''
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.queue = PriorityQueue(max_capacity)
        self.capacity = 0

    def add(self, priority, element):
        if self.capacity < self.max_capacity:
        # if not self.queue.full():
            self.queue.put((priority, element))
            self.capacity += 1
        elif self.queue.queue[0][0] < priority:
            self.queue.get()
            self.queue.put((priority, element))

    def get_reverse_sorted_elements(self):
        result_list = [None] * self.capacity

        for i in range(self.capacity - 1, -1, -1):
            result_list[i] = self.queue.get()[1]
        return result_list
