# some random python code


def foo():
    mylist = [(1, 'int'), (3, 'int'), (2, 'float'), (4, 'float')]
    types = {v for k, v in mylist}

    max_vals = {}
    for tp in {v for _, v in mylist}:
        def key(item):
            val, typ = item
            return val if typ == tp else 0
        max_vals[tp] = max(mylist, key=key)

    print('-' * 20)
    print([max(mylist, key=lambda item: item[0] if item[1] == tp else 0) 
           for tp in {v for _, v in mylist}])
    print('-' * 20)
        
    print([(k, v) for k, v in mylist if v == 'int'])
    print("MAX:VALS:", max_vals)
    max_values = {tp: 0 for tp in types}
    types = max_values.keys()

    print("TYPES:", types)

    print("TYPES:", types)

    # for value, data_type in mylist:
    #     max_values[data_type] = max(value, max_values[data_type])

    new_list = [(val, tp) for val, tp in mylist if max_values[tp] == val]

    print(new_list)
    print(max_values)
