def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(23, 14, 'plane' )
print_params(23, c = 14, b='plane' )
print_params(b = 25)
print_params(c=[1, 2, 3])

values_list = (True, 2, 'word')
values_dict = {'a': 1, 'b': True, 'c': "samsung"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('Ubisoft', 2000)
print_params(*values_list_2, 42)