company_name = input()
count_adult_ticket = int(input())
count_kid_ticket = int(input())
net_price_adult_ticket = float(input())
tax_service = float(input())

net_price_kid_ticket = net_price_adult_ticket - (0.7 * net_price_adult_ticket)

one_adult_ticket_price = net_price_adult_ticket + tax_service
one_kid_ticket_price = net_price_kid_ticket + tax_service

all_ticket_price = (one_adult_ticket_price * count_adult_ticket) + (one_kid_ticket_price * count_kid_ticket)
profit = all_ticket_price * 0.2

print(f"The profit of your agency from {company_name} tickets is {profit:.2f} lv.")
