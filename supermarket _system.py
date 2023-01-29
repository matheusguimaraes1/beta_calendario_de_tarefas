class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class CarrinhoCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, produto):
        self.produtos.remove(produto)

class Caixa:
    def __init__(self):
        self.carrinho = CarrinhoCompras()

    def calcular_preco_total(self):
        total = 0
        for produto in self.carrinho.produtos:
            total += produto.preco * produto.quantidade
        return total

    def imprimir_recibo(self):
        print("Recibo:")
        for produto in self.carrinho.produtos:
            print(f"{produto.nome}: R${produto.preco} x {produto.quantidade} = R${produto.preco * produto.quantidade}")
        print(f"Preço total: R${self.calcular_preco_total()}")

    def registrar_venda(self):
        # implemente a lógica para registrar a venda aqui (por exemplo, gravando em um arquivo)
        pass

# exemplo de uso
caixa = Caixa()
caixa.carrinho.adicionar_produto(Produto("Arroz", 5.0, 2))
caixa.carrinho.adicionar_produto(Produto("Feijão", 7.0, 1))
caixa.imprimir_recibo()
caixa.registrar_venda()
