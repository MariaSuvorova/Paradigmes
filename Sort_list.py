import random


def sort_imp(numbers):
    '''sort_list_imperative'''
    def _sort_imp(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _sort_imp(items, low, split_index)
            _sort_imp(items, split_index + 1, high)
    _sort_imp(numbers, 0, len(numbers) - 1)
    numbers.reverse()
    
def partition(numbers, low, high):
    pivot= numbers[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while numbers[i] < pivot:
            i += 1

        j -= 1
        while numbers[j] > pivot:
            j -= 1

        if i >= j:
            return j
        numbers[i], numbers[j] = numbers[j], numbers[i]

def sort_dec(numbers):
    '''sort_list_declarative'''
    if numbers == []:
        return []
    temp, sublist = numbers[0] ,numbers[1:]
    # в порядке возрастания:
    # return sort_dec([i for i in sublist if i<temp])+[temp]+sort_dec([i for i in sublist if i>=temp])
    # в порядке возрастания:
    return sort_dec([i for i in sublist if i>=temp])+[temp]+sort_dec([i for i in sublist if i<temp])

numbers=[random.randint(-100,100) for _ in range(11)]
print("numbers", numbers, '\n')
numbers1 = numbers.copy()
sort_imp(numbers)
print("sort_list_imperative", numbers, '\n')
print("sort_list_declarative", sort_dec(numbers1))
