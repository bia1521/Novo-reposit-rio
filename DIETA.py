quantidade_refeicoes, limite_calorias = map(int, input().split())

total = 0

for _ in range(quantidade_refeicoes):
    p, g, c = map(int, input().split())
    calorias = (p * 4) + (g * 9) + (c * 4)
    total += calorias

restante = limite_calorias - total
print(restante)