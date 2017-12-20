import datetime

# Book version
def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


# Alternative version:
def shell_sort(array):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    gap = len(array) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(array)):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 40]
    alist2 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 40]

    print('Unsorted list: {}'.format(alist))
    print()
    print('Book implementation of shell sort on a 10-element list: ')
    start = datetime.datetime.now()
    shellSort(alist)
    finish = datetime.datetime.now()
    print('Result: {}'.format(alist))
    print('Timing: {}'.format(finish - start))
    print()
    print('Alternative implementation of shell sort on a 10-element list: ')
    start = datetime.datetime.now()
    shell_sort(alist)
    finish = datetime.datetime.now()
    print('Result: {}'.format(alist))
    print('Timing: {}'.format(finish - start))
