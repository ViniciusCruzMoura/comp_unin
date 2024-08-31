def mostrar_cardapio():
    print("""
---Cardapio---
Tamanho | Bife Acebolado (BA) | File de Frango (FF)
P       | R$ 16.00            | R$ 15.00
M       | R$ 18.00            | R$ 17.00
G       | R$ 22.00            | R$ 21.00
--------------
""")

def calc_total_a_pagar(pedidos):
    total_a_pagar = 0
    valor_do_pedido = 0
    for pedido in pedidos:
        if pedido.get("sabor") == "BA":
            if pedido.get("tamanho") == "P":
                valor_do_pedido = 1600
            elif pedido.get("tamanho") == "M":
                valor_do_pedido = 1800
            elif pedido.get("tamanho") == "G":
                valor_do_pedido = 2200
        elif pedido.get("sabor") == "FF":
            if pedido.get("tamanho") == "P":
                valor_do_pedido = 1500
            elif pedido.get("tamanho") == "M":
                valor_do_pedido = 1700
            elif pedido.get("tamanho") == "G":
                valor_do_pedido = 2100
        else:
            valor_do_pedido = 0
            continue
        total_a_pagar += valor_do_pedido
    return total_a_pagar

def escolher_pedido():
    return {"sabor": None, "tamanho": None}

def main():
    # Vendas para uma loja que vende Marmitas de Bife Acebolado
    # ou Filé de Frango

    # Dados
    pedidos = []
    sabor = None
    tamanho = None
    novo_pedido = None
    total_a_pagar = None

    print("Bem Vindo ao Estabelecimento do Vinicius Eduardo Carvalho da Cruz de Moura")
    
    mostrar_cardapio()
    
    # Entrada de Valores do Usuario
    while True:
        while not sabor:
            sabor = input("Entre com o sabor desejado (BA/FF):").upper()
            if sabor != "BA" and sabor != "FF":
                print("Sabor Invalido!")
                sabor = None

        while not tamanho:
            tamanho = input("Entre com o tamanho desejado (P/M/G):").upper()
            if tamanho != "P" and tamanho != "M" and tamanho != "G":
                print("Tamanho Invalido!")
                tamanho = None
        # Persiste o Pedido
        pedidos.append({"sabor": sabor, "tamanho": tamanho})

        # Saida de Valores do Pedido
        print("Você pediu um", "File de Frango" if sabor == "FF" else "Bife Acebolado", "no tamanho de", tamanho)
        
        # Continuar ou Finalizar o Laço de Repetição de Pedidos
        while not novo_pedido:
            novo_pedido = input("Deseja algo mais? (s/N)").upper()
            if novo_pedido != "S" and novo_pedido != "N":
                print("Opção Invalido!")
                novo_pedido = None
        if novo_pedido == "N":
            break
        # Limpa as Variaveis Temporarias
        sabor = None
        tamanho = None
        novo_pedido = None

    # Todos os Pedidos
    total_a_pagar = calc_total_a_pagar(pedidos)
    print("O valor total a pagar:", "R$", "{0:.2f}".format(total_a_pagar/100))

if __name__ == '__main__':
    main()
