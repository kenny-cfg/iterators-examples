def even_numbers():
    count = 0
    while True:
        yield count
        count += 2


def even_numbers_limited(limit):
    count = 0
    while True:
        if count > limit:
            return
        yield count
        count += 2


if __name__ == '__main__':
    limited_iterator = even_numbers_limited(1000)
    for x in limited_iterator:
        print(x)
    # iterator = even_numbers()
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
