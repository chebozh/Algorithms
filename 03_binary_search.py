"""Binary search is a more efficient search algorithm which relies on the elements in the list being sorted. We apply
the same search process to progressively smaller sub-lists of the original list, starting with the whole list and
approximately halving the search area every time.

We first check the middle element in the list.

If it is the value we want, we can stop. If it is higher than the value we want, we repeat the search process with
the portion of the list before the middle element. If it is lower than the value we want, we repeat the search
process with the portion of the list after the middle element. """
import time

# Book version
def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# My (recursive) version
def binary_search(a_list, element):
    first = 0
    last = len(a_list) - 1
    if len(a_list) == 0:
        return False
    else:
        middle = (first + last) // 2
        if a_list[middle] == element:
            return True
        elif element < a_list[middle]:
            return binary_search(a_list[first:middle], element)
        else:
            return binary_search(a_list[middle + 1:last], element)


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print('Book version: ')
    start_time = time.time()
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
    print("--- %s seconds.---" % (time.time() - start_time))
    print('**' * 20)
    print('My version: ')
    start_time = time.time()
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))
    print("--- %s seconds.---" % (time.time() - start_time))

# Book version:
# False
# True
# --- 2.193450927734375e-05 seconds. ---
# ****************************************
# My version:
# False
# True
# --- 1.0967254638671875e-05 seconds.---


