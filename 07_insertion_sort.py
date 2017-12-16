"""The insertion sort, although still O(n^2), works in a slightly different way. It always maintains a sorted
sublist in the lower positions of the list. Each new item is then “inserted” back into the previous sublist such that
the sorted sublist is one item larger. """
import datetime


# Book version:
def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


# Alternative version:
def insertion_sort(bad_list):
    for index in range(1, len(bad_list)):
        value = bad_list[index]
        i = index - 1  # index of item on the left
        while i >= 0:
            if value < bad_list[i]:
                bad_list[i + 1] = bad_list[i]
                bad_list[i] = value
            else:
                break


# Shorter alternative version:
def insertion_sort2(bad_list):
    for index in range(1, len(bad_list)):
        value = bad_list[index]
        i = index - 1  # index of item on the left
        while i >= 0 and value < bad_list[i]:
            bad_list[i + 1] = bad_list[i]
            bad_list[i] = value


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    alist3 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print('Unsorted list: {}'.format(alist))
    print()
    print('Book version of insertion sort: ')
    start = datetime.datetime.now()
    insertionSort(alist)
    finish = datetime.datetime.now()
    print('Result: {}'.format(alist))
    print('Timing: {}'.format(finish - start))

    print()

    print('Alternative version of insertion sort: ')
    start = datetime.datetime.now()
    insertion_sort(alist2)
    finish = datetime.datetime.now()
    print('Result: {}'.format(alist))
    print('Timing: {}'.format(finish - start))

    print()

    print('Alternative version 2 of insertion sort: ')
    start = datetime.datetime.now()
    insertion_sort2(alist3)
    finish = datetime.datetime.now()
    print('Result: {}'.format(alist))
    print('Timing: {}'.format(finish - start))


# Timing results:
# Unsorted list: [54, 26, 93, 17, 77, 31, 44, 55, 20]
#
# Book version of insertion sort:
# Result: [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Timing: 0:00:00.000016
#
# Alternative version of insertion sort:
# Result: [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Timing: 0:00:00.000009
#
# Alternative version 2 of insertion sort:
# Result: [17, 20, 26, 31, 44, 54, 55, 77, 93]
# Timing: 0:00:00.000007
