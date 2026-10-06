#
# Author: 
# Student Number:
#
# Place the code for your lab 2 here.  Read the specs carefully.
#
# To test, run the following command:
#     python3 lab2_tester.py
#

# Write the following 3 functions recursively

def factorial(number):
    # your solution here
    if number <= 1:
        return 1
    return number * factorial(number - 1)



def linear_search(list, key):
    # your solution here
    def _linear_search_helper(lst, target, index):
        if index >= len(lst):
            return -1
        if lst[index] == target:
            return index
        return _linear_search_helper(list, target, index +1)
    return _linear_search_helper(list, key, 0)



def binary_search(list, key):
    # your solution here
    def _binary_search_helper(lst, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return _binary_search_helper(lst, target, low, mid -1)
        else:
            return _binary_search_helper(lst, target, mid +1, high)
    return _binary_search_helper(list, key, 0, len(list) -1)
