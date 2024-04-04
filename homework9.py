def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(5, 'слово',)
print_params(5, 'слово', False)
print_params(b='слово', c=False)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = [6, 'значение', True]
values_dict = {"a": 12, "b": 'строка', "c": True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [8, 'apple']
print_params(*values_list_2,42)