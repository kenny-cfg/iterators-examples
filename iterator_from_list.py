nums = [2, 4, 1, 9, 6]

nums_iter = iter(nums)

if __name__ == '__main__':
    print(nums_iter)
    for x in nums_iter: # Knows to stop
        print(x)

    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter))
    # print(next(nums_iter)) # Throws an exception

    # Alternative notation

    print(nums_iter.__next__())
    print(nums_iter.__next__())
    print(nums_iter.__next__())
    print(nums_iter.__next__())
    print(nums_iter.__next__())
    print(nums_iter.__next__()) # Throws an exception
