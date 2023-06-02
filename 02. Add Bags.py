price_of_baggage = float(input())
kg_of_baggage = int(input())
days_till_trip = int(input())
count_baggage = int(input())
tax = 0

if kg_of_baggage < 10:
    tax = price_of_baggage * 0.2
elif 10 <= kg_of_baggage <= 20:
    tax = price_of_baggage * 0.5
elif kg_of_baggage > 20:
    tax = price_of_baggage

if days_till_trip > 30:
    tax += tax * 0.1
elif 7 <= days_till_trip <= 30:
    tax += tax * 0.15
elif days_till_trip < 7:
    tax += tax * 0.4

sum_of_price = tax * count_baggage
print(f"The total price of bags is: {sum_of_price:.2f} lv. ")




