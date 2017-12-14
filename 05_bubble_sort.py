"""
Bubble sort
"""
import datetime


# Book version

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp


# Version 2
def bubble_sort(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i] > bad_list[i + 1]:
                sorted = False
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]


# Version 3
def bubble_sort2(bad_list):
    for passes_left in range(len(bad_list) - 1, 0, -1):
        for i in range(passes_left):
            if bad_list[i] > bad_list[i + 1]:
                bad_list[i], bad_list[i + 1] = bad_list[i + 1], bad_list[i]


# Short Bubble sort
"""if during a pass there are no exchanges, then we know that the list must be sorted. A bubble sort can be modified 
to stop early if it finds that the list has become sorted. This means that for lists that require just a few passes, 
a bubble sort may have an advantage in that it will recognize the sorted list and stop. Code bello as well as 
 Version 2 work similarly"""


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum = passnum - 1


# Timing tests
if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    a_list2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    a_list3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print('Book version: ')
    start = datetime.datetime.now()
    bubbleSort(a_list)
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print(a_list)

    print('version 2: ')
    start = datetime.datetime.now()
    bubble_sort(a_list2)
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print(a_list)

    print('version 3: ')
    start = datetime.datetime.now()
    bubble_sort2(a_list3)
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print(a_list)

    print('----------------Short Bubble sorts----------------')
    sorted_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
    sorted_list2 = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]

    print('Short bubble sort book version:')
    start = datetime.datetime.now()
    shortBubbleSort(sorted_list)
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print(sorted_list)

    print(' short bubble sort - Version 2')
    start = datetime.datetime.now()
    bubble_sort(sorted_list2)
    finish = datetime.datetime.now()
    print("--- %s ---" % (finish - start))
    print(sorted_list)

#  Subjective results:
# Book version:
# --- 0:00:00.000029 ---
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# version 2:
# --- 0:00:00.000027 ---
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# version 3:
# --- 0:00:00.000022 ---
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
# ----------------Short Bubble sorts----------------
# Short bubble sort book version:
# --- 0:00:00.000012 ---
# [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
#  short bubble sort - Version 2
# --- 0:00:00.000009 ---
# [20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
