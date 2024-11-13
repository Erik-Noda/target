def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char+ invertida
    return invertida

original = "OLAA"
invertida = inverter_string(original)
print(invertida)