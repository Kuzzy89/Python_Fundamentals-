str_money = input().split(", ")
beggars_count = int(input())

beggars = [0] * beggars_count

for i in range(len(str_money)):
    beggars_i = i % beggars_count
    money = int(str_money[i])
    beggars[beggars_i] += money

print(beggars)
