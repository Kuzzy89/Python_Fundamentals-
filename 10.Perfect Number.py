def Perfect_Number(Number):
    Sums = 0
    for i in range(1, Number):
        if Number % i == 0:
            Sums = Sums + i
    return Sums


Numb = int(input())
if (Numb == Perfect_Number(Numb)):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")