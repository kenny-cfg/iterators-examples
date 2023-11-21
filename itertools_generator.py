import itertools

if __name__ == '__main__':
    all_squares = (x * x for x in itertools.islice(itertools.count(), 1, None))
    all_evens = (2 * x for x in itertools.islice(itertools.count(), 1, None))
    zipped = (x for sublist in zip(all_squares, all_evens) for x in sublist)
    count = 10
    for x in zipped:
        print(x)
        count -= 1
        if count < 0:
            break
    # square_numbers_limited = (x * x for x in itertools.islice(all_positive_integers(), 10))
    # for x in square_numbers_limited:
    #     print(x)
