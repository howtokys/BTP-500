#
# Author: Thuong Tuyen Tran	
# Student Email: tttran56@myseneca.ca
#
# Place the code for your lab 5 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab5.py
#



class MinHeap:

	def __init__(self, inital_data = None):
		if inital_data is not None:
			self._data = list(inital_data)
			self._make_heap()
		else:
			self._data = []

	def _make_heap(self):
		for i in range(len(self._data) // 2 - 1, -1, -1):
			self._sift_down(i)

	def _sift_up(self, index):
		while index > 0:
			parent = (index - 1) // 2
			if self._data[index] < self._data[parent]:
				self._data[index], self._data[parent] = self._data[parent], self._data[index]
				index = parent
			else:
				break

	def _sift_down(self, index):
		n = len(self._data)
		while True:
			smallest = index
			left = 2 * index + 1
			right = 2 * index + 2

			if left < n and self._data[left] < self._data[smallest]:
				smallest = left
			if right < n and self._data[right] < self._data[smallest]:
				smallest = right

			if smallest != index:
				self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
				index = smallest
			else:
				break

	def is_empty(self):
		return len(self._data) == 0

	def size(self):
		return len(self._data)

	def push(self, data):
		self._data.append(data)
		self._sift_up(len(self._data) - 1)

	def pop(self):
		if self.is_empty():
			return None

		min_val = self._data[0]
		last_val = self._data.pop()

		if not self.is_empty():
			self._data[0] = last_val
			self._sift_down(0)

		return min_val

	def min(self):
		if self.is_empty():
			return None
		return self._data[0]

