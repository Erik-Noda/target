def pertence(numero):
    if numero<0:
        return False
    
    def quadrado_perfeito(valor):
        raiz  = (valor**0.5)
        return raiz*raiz==valor
    
    return quadrado_perfeito(5*numero*numero + 4) or quadrado_perfeito(5*numero*numero-4)

numero = int(input("Numero: "))

if pertence(numero):
    print(f"{numero} pertence a sequencia de fibonacci")
else:
    print(f"{numero} nao pertence a sequencia de fibonacci" )