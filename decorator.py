class Bebida:
    def descricao(self):
        raise NotImplementedError("Subclasse deve implementar descricao()")

    def custo(self):
        raise NotImplementedError("Subclasse deve implementar custo()")


class Cafe(Bebida):
    def descricao(self):
        return "Cafe"

    def custo(self):
        return 5.00


class Cha(Bebida):
    def descricao(self):
        return "Cha"

    def custo(self):
        return 4.00


class Cappuccino(Bebida):
    def descricao(self):
        return "Cappuccino"

    def custo(self):
        return 7.00


class Suco(Bebida):
    def descricao(self):
        return "Suco"

    def custo(self):
        return 6.00


class DecoradorBebida(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida

    def descricao(self):
        return self.bebida.descricao()

    def custo(self):
        return self.bebida.custo()


class ComLeite(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " + Leite"

    def custo(self):
        return self.bebida.custo() + 2.00


class ComChocolate(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " + Chocolate"

    def custo(self):
        return self.bebida.custo() + 3.00


class ComChantilly(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " + Chantilly"

    def custo(self):
        return self.bebida.custo() + 2.50


class ComCaramelo(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " + Caramelo"

    def custo(self):
        return self.bebida.custo() + 1.50


class ComCanela(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " + Canela"


class SemAcucar(DecoradorBebida):
    def descricao(self):
        return self.bebida.descricao() + " (Sem Acucar)"

    def custo(self):
        return self.bebida.custo()


DRINKS = {
    "1": ("Cafe",       Cafe,       5.00),
    "2": ("Cha",        Cha,        4.00),
    "3": ("Cappuccino", Cappuccino, 7.00),
    "4": ("Suco",       Suco,       6.00),
}

ADICIONAIS = {
    "1": ("Leite",               ComLeite),
    "2": ("Chocolate",           ComChocolate),
    "3": ("Chantilly",           ComChantilly),
    "4": ("Caramelo",            ComCaramelo),
    "5": ("Canela",              ComCanela),
    "6": ("Sem Acucar (R$ 0.00)", SemAcucar),
}


print("=== Cafeteria ===")
print("Escolha o drink base:")
print("1 - Cafe       (R$ 5.00)")
print("2 - Cha        (R$ 4.00)")
print("3 - Cappuccino (R$ 7.00)")
print("4 - Suco       (R$ 6.00)")

opcao_drink = ""
pedido = None

while pedido is None:
    opcao_drink = input("\nDrink: ")
    if opcao_drink in DRINKS:
        nome, classe, preco = DRINKS[opcao_drink]
        pedido = classe()
        print("Drink escolhido: " + nome + " (R$ %.2f)" % preco)
    else:
        print("Opcao invalida. Tente 1, 2, 3 ou 4.")


print("\nAgora escolha os adicionais:")
print("1 - Leite               (+ R$ 2.00)")
print("2 - Chocolate           (+ R$ 3.00)")
print("3 - Chantilly           (+ R$ 2.50)")
print("4 - Caramelo            (+ R$ 1.50)")
print("5 - Canela              (+ R$ 0.00)")
print("6 - Sem Acucar          ( R$ 0.00)")
print("0 - Finalizar pedido")

opcao = ""
while opcao != "0":
    print("\nPedido atual: " + pedido.descricao())
    print("Total parcial: R$ %.2f" % pedido.custo())
    opcao = input("Adicional: ")

    if opcao in ADICIONAIS:
        nome, classe = ADICIONAIS[opcao]
        pedido = classe(pedido)
        print("Adicionado: " + nome)
    elif opcao == "0":
        print("\n=== Pedido Final ===")
        print("Descricao: " + pedido.descricao())
        print("Total:     R$ %.2f" % pedido.custo())
    else:
        print("Opcao invalida.")
