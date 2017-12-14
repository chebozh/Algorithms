import datetime


# Book version
def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


# Version 2
def selection_sort(l):
    for i in range(len(l)):
        max_el = max(l[:len(l) - i])
        max_index = l.index(max_el)
        l[len(l) - i - 1], l[max_index] = l[max_index], l[len(l) - i - 1]  # swaps


# Version 3
def selection_sort2(the_list):
    for i in range(len(the_list) - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if the_list[j] > the_list[max_index]:
                max_index = j
            the_list[i], the_list[max_index] = the_list[max_index], the_list[i]


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print('List to sort: {}'.format(alist))
print('Book example')
start = datetime.datetime.now()
selectionSort(alist)
finish = datetime.datetime.now()
print("--- %s ---" % (finish - start))
print(alist)
print()
print('Version2: ')
start = datetime.datetime.now()
selection_sort(alist2)
finish = datetime.datetime.now()
print("--- %s ---" % (finish - start))
print('Sorted list: {}'.format(alist2))
print()
print('Version3: ')
start = datetime.datetime.now()
selection_sort2(alist3)
finish = datetime.datetime.now()
print("--- %s ---" % (finish - start))
print('Sorted list: {}'.format(alist3))


# Timings:
# List to sort: [54, 26, 93, 17, 77, 31, 44, 55, 20]
# Book example
# --- 0:00:00.000020 ---
# [17, 20, 26, 31, 44, 54, 55, 77, 93]
#
# Version2:
# --- 0:00:00.000023 ---
# Sorted list: [17, 20, 26, 31, 44, 54, 55, 77, 93]
#
# Version3:
# --- 0:00:00.000018 ---
# Sorted list: [17, 20, 26, 31, 44, 54, 55, 77, 93]
