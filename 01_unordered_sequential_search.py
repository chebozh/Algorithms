"""Sequential search Starting at the first item in the list, we simply move from item to item, following the
underlying sequential ordering until we either find what we are looking for or run out of items. If we run out of
items, we have discovered that the item we were searching for was not present.
Worst case complexity O(n):
"""
import datetime


# Book example:


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


# Alternative (slightly faster) version:
def sequential_search(a_list, element):
    for n in a_list:
        if n == element:
            return True
    return False


# Checks
if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print('Book version: ')
    start = datetime.datetime.now()
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print('**' * 20)
    print('Alternative version: ')
    start = datetime.datetime.now()
    print(sequential_search(testlist, 3))
    print(sequential_search(testlist, 13))
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))

# Results after a few runs:
# Book version:
# False
# True
# --- 0:00:00.000038 ---
# ****************************************
# Alternative version:
# False
# True
# --- 0:00:00.000017 ---

