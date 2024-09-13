import random

def random_list(length):
    list = []

    for _ in range(length):
        list.append(random.randint(1, 100))

    return list

def is_sorted(list):
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def quick_sort(list):
    if len(list) <= 1:
        return list
    
    pivot = list[0]
    left, right = [], []

    for value in list[1:]:
        if value < pivot:
            left.append(value)
        else:
            right.append(value)

    return quick_sort(left) + [pivot] + quick_sort(right)

def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left, right = list[:mid], list[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    sorted = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    while i < len(left):
        sorted.append(left[i])
        i += 1
        
    while j < len(right):
        sorted.append(right[j])
        j += 1
        
    return sorted

def selection_sort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
    
        list[i], list[min] = list[min], list[i]

    return list

def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        min = i

        while min > 0 and temp < list[min - 1]:
            list[min] = list[min - 1]
            min -= 1

        list[min] = temp
    
    return list

def bubble_sort(list):
    swaps = 0

    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp

            swaps += 1

    if swaps > 0:
        return bubble_sort(list)
    else:
        return list

test = random_list(random.randint(1, 50))

print('Sort Methods Validation:')
print('Random Input: %s' % test)
print('Expected Output: %s' % quick_sort((test.copy())))
print('Quick: %s' % is_sorted(quick_sort(test.copy())))
print('Merge: %s' % is_sorted(merge_sort(test.copy())))
print('Selection: %s' % is_sorted(selection_sort(test.copy())))
print('Insertion: %s' % is_sorted(insertion_sort(test.copy())))
print('Bubble: %s' % is_sorted(bubble_sort(test.copy())))
