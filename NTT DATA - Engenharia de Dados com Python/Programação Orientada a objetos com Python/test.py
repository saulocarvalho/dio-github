class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)
        else:
            raise TypeError("Erro: O objeto precisa ser uma instância da classe Venda")

    def total_vendas(self):
        total = sum(venda.quantidade * venda.valor for venda in self.vendas)
        return total

def main():
    categorias = []

    # Supondo que a entrada é de 2 categorias, cada uma com 2 vendas
    num_categorias = 2
    num_vendas_por_categoria = 2

    for _ in range(num_categorias):
        nome_categoria = input().strip()
        categoria = Categoria(nome_categoria)

        for _ in range(num_vendas_por_categoria):
            entrada_venda = input().strip()
            if not entrada_venda:
                continue
            produto, quantidade, valor = entrada_venda.split(',')
            quantidade = int(quantidade.strip())
            valor = float(valor.strip())
            
            venda = Venda(produto.strip(), quantidade, valor)
            categoria.adicionar_venda(venda)
        
        categorias.append(categoria)
    
    # Exibindo os totais de vendas para cada categoria
    for categoria in categorias:
        total = categoria.total_vendas()
        print(f"Vendas em {categoria.nome}: {total:.1f}")

if __name__ == "__main__":
    main()
