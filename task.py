
def multiplication_table(n):
    '''таблица умножения всех чисел от 1 до n'''
    # for i in range(1, n+1):
    #     print("1 *",i, " = ", i)
    print(*[f"1 * {i} = {i} \n" for i in range(1, n+1)])

multiplication_table(19)
multiplication_table(7)
    