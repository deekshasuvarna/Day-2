''' program to find the sum of the given elements of the list . '''

from functools import reduce

li = [1,2,3,4,5,6,7,8,9]

sum = reduce(lambda a , b : a + b , li)

print(sum)
