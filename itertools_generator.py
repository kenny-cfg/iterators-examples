def all_positive_integers():
    number_to_return = 1
    while True:
        yield number_to_return
        number_to_return += 1


if __name__ == '__main__':
    count = 10
    for x in all_positive_integers():
        print(x)
        count -= 1
        if count < 0:
            break
