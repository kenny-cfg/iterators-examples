# Write an iterator as a class that returns the square numbers but stops at 100

class SquareNumbersLimited:
    def __init__(self):
        self.number_to_square = 1

    def __iter__(self):
        self.number_to_square = 1
        return self

    def __next__(self):
        number_to_square = self.number_to_square
        self.number_to_square += 1
        if number_to_square > 10:
            raise StopIteration
        return number_to_square * number_to_square


if __name__ == "__main__":
    iterator = SquareNumbersLimited()
    for x in iterator:
        print(x)

    count = 10
    for x in iterator:
        print(x)
