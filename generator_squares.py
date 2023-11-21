# Write a generator that returns the square numbers (1, 4, 9, 16, ...)
# Write a generator that returns the square numbers but stops at 100

def square_numbers():
    current_number = 1
    while True:
        yield current_number * current_number
        current_number += 1


if __name__ == '__main__':
    count = 10
    for x in square_numbers():
        print(x)
        count -= 1
        if count < 0:
            break