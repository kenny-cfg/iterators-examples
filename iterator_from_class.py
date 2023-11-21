class EvenNumbers:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        next_num = self.num
        self.num += 2
        return self.num


if __name__ == "__main__":
    iterator = EvenNumbers()
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

    another_iterator = EvenNumbers()
    for x in another_iterator:
        print(x)

