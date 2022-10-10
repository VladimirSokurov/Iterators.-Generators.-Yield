nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(list_):
    while list_:
        new_list = [x for sublist in list_ for x in sublist]
        for i in new_list:
            yield i
        break


for item in flat_generator(nested_list):
    print(item)
