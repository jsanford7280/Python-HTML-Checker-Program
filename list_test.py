import random
import time
import timeit

## Setting up the Python list
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

## Unordered list
class UnorderedList(object):
    def __init__(self):
        self.N = 0
        self.head = None

    def size(self):
        return self.N

    def is_empty(self):
        return self.N == 0

    def add(self, data):
        self.N += 1
        temp = Node(data)
        temp.set_next(self.head)
        self.head = temp

    def search(self, data):
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == data:
                found = True
            current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        while current.get_data() != item:
            previous = current
            current = current.get_next()
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        self.N -= 1

## Output for the program run time
def Program():
    y = 3.1415
    for x in range(100):
        y = y ** 0.7
    return y
print()
print('The program run time is: ')
print(timeit.timeit(Program, number=100000))


## Outputs the python list and linked list run times for compare
for i in range(1000, 100000001, 100000):
    list1 = list(range(i))
    list2 = UnorderedList()
    for a in range(i):
        list2.add(a) 

    a = random.randrange(0, i)

    start_time1 = time.time()
    list1.remove(a)
    end_time1 = time.time()

    start_time2 = time.time()
    list2.remove(a)
    end_time2 = time.time()
    print("Python List time: {0}. Linked List time: {1}".format(end_time1-start_time1, end_time2-
start_time2))
