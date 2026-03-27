from functools import reduce

numbers = [1,2,3,4,5]

square = list(map(lambda x: x*x, numbers))
print("Map:", square)

even = list(filter(lambda x: x%2==0, numbers))
print("Filter:", even)

product = reduce(lambda a,b: a*b, numbers)
print("Reduce:", product)