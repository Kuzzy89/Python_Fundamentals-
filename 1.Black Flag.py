days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

plunder = 0

for n in range(1, days + 1):
    plunder += daily_plunder

    if n % 3 == 0:
        plunder += (daily_plunder * 0.5)

    if n % 5 == 0:
        plunder -= (plunder * 0.3)


if plunder >= expected_plunder:
    print(f"Ahoy! {plunder:.2f} plunder gained.")
else:
    re = (plunder / expected_plunder) * 100
    print(f"Collected only {re:.2f}% of the plunder.")
