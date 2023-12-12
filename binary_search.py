def binary_search(numbers,n):
    '''Вспомогательная функция'''
    first = 0
    last = len(numbers)-1
    result = binary_search_alg(numbers, first, last, n)
    if result == "-1":
        return f"-1 (элемент {n} не найден)"
    else:
        return f"{n} имеет индекс {result}"
    
def binary_search_alg(numbers, first, last, n):
    '''Рекурсивная функция'''
    if last >= first:
        mid = (first + last) // 2
        mid_elem = numbers[mid]
        if mid_elem == n:
            return mid
            # return f"{n} имеет индекс {mid}"
        elif mid_elem > n:  # центральный элемент больше искомого
            # отсекаем правую часть списка
            new_border = mid - 1
            return binary_search_alg(numbers, first, new_border, n)
        elif mid_elem < n:  # центральный элемент меньше искомого
            # отсекаем левую часть списка
            new_border = mid + 1
            return binary_search_alg (numbers, new_border, last, n)
    else:
        return "-1"
numbers = [3,8,12,15,18,45,77,89]
print(numbers)
n = 15
print(binary_search(numbers,n))
n = 77
print(binary_search(numbers,n))
n = 78
print(binary_search(numbers,n))
