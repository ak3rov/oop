letters = []
numbers = []
data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
numbers.remove(6.13)
numbers.insert(2,2)
numbers.sort()
letters.reverse()
letters.remove('g')
letters.remove('C')
letters.insert(0,'G')
letters.insert(6,'c')
numbers = (1 **2),(2**2),(3**2)
tuple1 = tuple(letters)
tuple2 = tuple(numbers)
print(tuple1,tuple2)