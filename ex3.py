import json


with open("faturamento.json") as f:
    faturamento_diario = json.load(f)

faturamento_valido = [f for f in faturamento_diario if f>0]

menor = min(faturamento_valido)
maior = max(faturamento_valido)

media_faturamento = sum*(faturamento_diario) / len(faturamento_valido)

dias_acima = sum(1 for f in faturamento_valido if f>media_faturamento)

print("menor: ",menor)
print("maior: ",maior)
print("dias acima da media: ",dias_acima)