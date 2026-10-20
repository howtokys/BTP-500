#
# Author: Thuong Tuyen Tran
# Student Number: 161527239
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#


class DoublyLinked:

    class Node:
        def __init__(self, data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self, data = None):
        self.head = None
        self.tail = None
        if data is not None:
            self.push_back(data)

    def get_front(self):
        return self.head

    def get_back(self):
        return self.tail

    def push_front(self, data):
        new_node = self.Node(data, next=self.head, prev=None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node

    def push_back(self, data):
        new_node = self.Node(data, next=None, prev=self.tail)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_front(self):
        if self.head is None:
            raise IndexError('pop_front() used on empty list')
        data = self.head.get_data()
        self.head = self.head.get_next()
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        return data

    def pop_back(self):
        if self.tail is None:
            raise IndexError('pop_back() used on empty list')
        data = self.tail.get_data()
        self.tail = self.tail.get_previous()
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return data


class Sentinel:

    class Node:
        def __init__(self, data = None, next = None, prev = None):
            self.data = data
            self.next = next
            self.prev = prev

        def get_data(self):
            return self.data

        def get_next(self):
            return self.next

        def get_previous(self):
            return self.prev

    def __init__(self, data = None):
        self.header = self.Node(None)
        self.trailer = self.Node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        if data is not None:
            self.push_back(data)

    def get_front(self):
        if self.header.next == self.trailer:
            return None
        return self.header.next

    def get_back(self):
        if self.trailer.prev == self.header:
            return None
        return self.trailer.prev

    def push_front(self, data):
        first = self.header.next
        new_node = self.Node(data, next=first, prev=self.header)
        self.header.next = new_node
        first.prev = new_node

    def push_back(self, data):
        last = self.trailer.prev
        new_node = self.Node(data, next=self.trailer, prev=last)
        last.next = new_node
        self.trailer.prev = new_node

    def pop_front(self):
        if self.header.next == self.trailer:
            raise IndexError('pop_front() used on empty list')
        first = self.header.next
        data = first.get_data()
        second = first.next
        self.header.next = second
        second.prev = self.header
        return data

    def pop_back(self):
        if self.trailer.prev == self.header:
            raise IndexError('pop_back() used on empty list')
        last = self.trailer.prev
        data = last.get_data()
        second_last = last.prev
        second_last.next = self.trailer
        self.trailer.prev = second_last
        return data






