def check_palindrome(lst):
    for num in lst:
        if str(num) == str(num)[::-1]:
            print(True)
        else:
            print(False)
    return


list_1 = input().split(", ")
check_palindrome(list_1)

# nums = [int(el) for el in input().split(", ")]