maznini = int(input()) * 0.01
proteini = int(input()) * 0.01
wuglehidrati = int(input()) * 0.01

ob6t_broi_kalorii = int(input())
procent_voda = int(input())

all_maznini = (ob6t_broi_kalorii * maznini) / 9
all_proteini = (ob6t_broi_kalorii * proteini) / 4
all_wuglehidrati = (ob6t_broi_kalorii * wuglehidrati) / 4

all_food = all_maznini + all_proteini + all_wuglehidrati

calorii_za_edin_gram = ob6t_broi_kalorii / all_food

gram_kaloriq = ((100 - procent_voda) * 0.01) * calorii_za_edin_gram

print(f"{gram_kaloriq:.4f}")
