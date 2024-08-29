from decimal import Decimal

def calc_valor_da_parcela(valor_do_pedido, juros, quantidade_de_parcelas):
    return round( (valor_do_pedido * ((100+juros)/100) ) / quantidade_de_parcelas , 2 )

def calc_valor_total_da_parcela(valor_da_parcela, quantidade_de_parcelas):
    return round( valor_da_parcela * quantidade_de_parcelas , 2)

def calc_porcentagem_de_juros(quantidade_de_parcelas):
    if quantidade_de_parcelas < 4:
        return 0
    elif quantidade_de_parcelas >= 4 and quantidade_de_parcelas < 6:
        return 4
    elif quantidade_de_parcelas >= 6 and quantidade_de_parcelas < 9:
        return 8
    elif quantidade_de_parcelas >= 9 and quantidade_de_parcelas < 13:
        return 16
    elif quantidade_de_parcelas >= 13:
        return 32
    return None

def converter_valor_monetario_para_inteiro(valor):
    return int(Decimal(valor) * 100)

def input_numerico(texto):
    val = None
    while True:
        try:
            val = input(texto)
            val = str(val).replace(",", ".")
            val = int(Decimal(val))
        except Exception:
            print("Valor invalido, porfavor digite um valor numerico valido!")
            continue
        break
    return val

def main():
    # Cobrar um Juros maior conforme a quantidade de parcelas que o
    # cliente deseja

    # Dados
    valor_do_pedido = None
    quantidade_de_parcelas = None
    juros = None
    valor_da_parcela = None
    valor_total_da_parcela = None

    print("Bem Vindo ao Estabelecimento do Vinicius Eduardo Carvalho da Cruz de Moura")

    # Entradas de Valores do Usuario
    valor_do_pedido = input_numerico("Entre com o valor do pedido:")
    quantidade_de_parcelas = input_numerico("Entre com a quantidade de parcelas:")

    # Calculo de Juros a Aplicar a Parcela
    juros = calc_porcentagem_de_juros(quantidade_de_parcelas)
    valor_da_parcela = calc_valor_da_parcela(valor_do_pedido, juros, quantidade_de_parcelas)
    valor_total_da_parcela = calc_valor_total_da_parcela(valor_da_parcela, quantidade_de_parcelas)

    # Saida de Valores
    print("O valor da parcela é de: {0:.2f}".format(valor_da_parcela))
    print("O valor total parcelado é de: {0:.2f}".format(valor_total_da_parcela))

    #print("Entre com o valor do pedido: 1000.0")
    #print("Entre com a quantidade de parcelas: 14")
    #print("O valor das parcelas é de: R$ 94.29")
    #print("O valor total parcelado é de: R$ 1320.00")

if __name__ == '__main__':
    main()
