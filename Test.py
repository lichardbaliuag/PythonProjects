
dict = {'a':'apple','b':'orange','c':'mango','d':'lemon'}

for x in dict:
    val = dict[x]
    dict[x] = val.upper()

    print('Change what', x, 'points to from', val, 'to', dict[x])


