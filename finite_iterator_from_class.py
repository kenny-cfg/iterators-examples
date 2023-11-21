class EvenNumbers2:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        self.num += 2
        if self.num >= 10:
            raise StopIteration
        return self.num


if __name__ == "__main__":
    iterator = EvenNumbers2()
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator))
    # print(next(iterator)) # Throws an exception

    another_iterator = EvenNumbers2()
    for x in another_iterator:
        print(x)

