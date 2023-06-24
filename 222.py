# •	Любовно послание - 0.60 лв.
# •	Восъчна роза - 7.20 лв.
# •	Ключодържател - 3.60 лв.
# •	Карикатура - 18.20 лв.
# •	Късмет изненада - 22 лв

cena_na_mominskoto_parti = float(input())
lubowno_poslanie = int(input())
wosu4na_fig = int(input())
klu4odurjatel = int(input())
karikatura = int(input())
kusmet_iznenada = int(input())

lubowno_poslanie_cena = lubowno_poslanie * 0.6
wosu4na_fig_cena = wosu4na_fig * 7.2
klu4odurjatel_cena = klu4odurjatel * 3.6
karikatura_cena = karikatura * 18.2
kusmet_iznenada_cena = kusmet_iznenada * 22

cqla_suma_artikuli = lubowno_poslanie_cena + wosu4na_fig_cena + klu4odurjatel_cena + karikatura_cena + kusmet_iznenada_cena
broi_artikuli = lubowno_poslanie + wosu4na_fig + klu4odurjatel + karikatura + kusmet_iznenada

if broi_artikuli >= 25:
    otstupka = cqla_suma_artikuli * 0.35
    cqla_suma_artikuli = cqla_suma_artikuli - otstupka

razhod_hosting = cqla_suma_artikuli * 0.1
pe4alba = cqla_suma_artikuli - razhod_hosting

diff = abs(pe4alba - cena_na_mominskoto_parti)

if cena_na_mominskoto_parti <= pe4alba:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")




