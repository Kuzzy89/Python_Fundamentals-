teglo_na_pratkata = float(input())
tip_usluga = input()
razstoqnie = int(input())

cena_1_km = 0
if tip_usluga == "standard":
    if teglo_na_pratkata <= 1:
        cena_1_km = 0.03
    if 1 < teglo_na_pratkata <= 10:
        cena_1_km = 0.05
    if 10 < teglo_na_pratkata <= 40:
        cena_1_km = 0.10
    if 40 < teglo_na_pratkata <= 90:
        cena_1_km = 0.15
    if 90 < teglo_na_pratkata <= 150:
        cena_1_km = 0.20

elif tip_usluga == "express":

    if teglo_na_pratkata <= 1:
         cena_1_km = teglo_na_pratkata * (0.03 * 0.8) + 0.03
    if 1 < teglo_na_pratkata <= 10:
         cena_1_km = 0.05 + teglo_na_pratkata * (0.05 * 0.4)
    if 10 < teglo_na_pratkata <= 40:
         cena_1_km = 0.10 + teglo_na_pratkata * (0.1 * 0.05)
    if 40 < teglo_na_pratkata <= 90:
         cena_1_km = 0.15 + teglo_na_pratkata * (0.15 * 0.02)
    if 90 < teglo_na_pratkata <= 150:
         cena_1_km = 0.20 + teglo_na_pratkata * (0.2 * 0.01)


kraina_cena = razstoqnie * cena_1_km
print(f"The delivery of your shipment with weight of {teglo_na_pratkata:.3f} kg. would cost {kraina_cena:.2f} lv.")

