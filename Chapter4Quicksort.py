def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0] # best to choose a random element as the pivot
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def findMaximumNumber(items):
    """ Exercise 4.3 """
    """
    Answer in book
    def max(list):
        if len(list) == 2:
            return list[0] if list[0] > list[1] else list[1]
        sub_max = max(list[1:])
        return list[0] if list[0] > sub_max else sub_max
    """
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] if items[0] > items[1] else items[1]
    sub_max = max(items[1:])
    return items[0] if items[0] > sub_max else sub_max


def countItemsInList(lst):
    """ Exercise 4.2 """
    """
    Answer in book
    def count(list):
        if list == []:
            return 0
        return 1 + count(list[1:])
    """
    if lst is None:  # base case
        return 0

    if len(lst) == 1:  # base case
        return 1

    return 1 + countItemsInList(removeFirstElement(lst))


def add(arr):
    """ Exercise 4.1 """
    """
    Answer in book
    def sum(list):
        if list == []:
            return 0
        return list[0] + sum(list[1:])
    """
    if arr is None:  # base case
        return 0

    if len(arr) == 1:  # base case
        return arr[0]

    return arr[0] + add(removeFirstElement(arr))


def removeFirstElement(old_list):
    new_list = []
    if len(old_list) > 1:
        for i in range(1, len(old_list)):
            new_list.append(old_list[i])
    else:
        new_list.append(old_list)
    return new_list