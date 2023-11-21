# Write an iterator as a class that returns the square numbers (1, 4, 9, 16, ...)
# Write an iterator as a class that returns the square numbers but stops at 100

class SquareNumbers:
    def __init__(self):
        self.number_to_square = 1

    def __iter__(self):
        self.number_to_square = 1
        return self

    def __next__(self):
        number_to_square = self.number_to_square
        self.number_to_square += 1
        return number_to_square * number_to_square


if __name__ == "__main__":
    iterator = SquareNumbers()
    count = 10
    for x in iterator:
        if count < 0:
            break
        print(x)
        count -= 1

    count = 10
    for x in iterator:
        if count < 0:
            break
        print(x)
        count -= 1
