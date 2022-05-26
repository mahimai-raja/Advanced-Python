from functools import reduce

nested_list = [[1,2,3],[4,5,6]]

combied_list = reduce(lambda x, y : x + y , nested_list)

print(combied_list)