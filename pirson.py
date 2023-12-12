from math import sqrt


def pirson(list1, list2):
    '''Pirson correlation function'''
    n = len(list1)
    mid1 = sum(list1)/n
    mid2 = sum(list2)/n
    upper_part = sum((num1-mid1)*(num2-mid2) for num1,num2 in zip(list1,list2))
    under_part_1 = sum((num1-mid1)**2 for num1 in list1)
    under_part_2 = sum(pow((num2-mid2),2) for num2 in list2)
    under_part = sqrt(under_part_1*under_part_2)
    # under_part = sqrt(sum((num1-mid1)**2)*sum((num2-mid2)**2) for num1,num2 in zip(list1,list2))
    return upper_part/under_part

x=[1,2,3]
y=[4,5,6]
print(pirson(x,y))

x=[1,2,3]
y=[4,5,30]
print("%.4f" % pirson(x,y))

x=[1,2,3]
y=[4,20,30]
print(f"{pirson(x,y):.4f}")
