"""Introducing some ordering to the underlying data on which sequential serach is applied. The list of items is
constructed so that the items are in ascending order, from low to high. If the item we are looking for is present in
the list, the chance of it being in any one of the n positions is still the same as before. We will still have the
same number of comparisons to find the item. However, if the item is not present there is a slight advantage. This is
because as soon as the search encounters an item larger than the one looked fore it stops, not having to make a
comparison with any other elements. =>  a sequential search is  improved by ordering the list only in the case where
we do not find the item. """
import datetime

# Book version


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found


# Alternative version (slightly faster according to timing test bellow):
def ordered_sequential_search(a_list, element):
    for n in a_list:
        if n == element:
            return True
        else:
            if n > element:
                return False
    return False

# Tests
if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print('Book version: ')
    start = datetime.datetime.now()
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print('**' * 20)
    print('Alternative version:')
    start = datetime.datetime.now()
    print(ordered_sequential_search(testlist, 3))
    print(ordered_sequential_search(testlist, 13))
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))

# Timings
# Book version:
# False
# True
# --- 0:00:00.000030 ---
# ****************************************
# My version:
# False
# True
# --- 0:00:00.000014 ---
