def printTrib(n):

    # Initialize first
    # three numbers
    first = 1
    second = 1
    third = 2

    print(first, "", end="")
    if (n > 1):
        print(second, "", end="")
    if (n > 2):
        print(third, "", end="")

        for i in range(3, n):
            curr = first + second + third
            first = second
            second = third
            third = curr

            print(curr, "", end="")


n = int(input())
printTrib(n)