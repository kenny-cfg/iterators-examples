import itertools


def all_positive_integers():
    number_to_return = 1
    while True:
        yield number_to_return
        number_to_return += 1


if __name__ == '__main__':
    square_numbers = (x * x for x in all_positive_integers())
    # count = 10
    # for x in square_numbers:
    #     print(x)
    #     count -= 1
    #     if count < 0:
    #         break
    square_numbers_limited = (x * x for x in itertools.islice(all_positive_integers(), 10))
    for x in square_numbers_limited:
        print(x)
