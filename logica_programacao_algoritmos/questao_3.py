from decimal import Decimal

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

def escolha_modelo():
    modelo = None

    # Pergunta o modelo desejado
    # Repete a pergunta se digitar uma opção diferente de: MCS/MLS/MCE/MLE
    while not modelo:
        modelo = input("""
Entre com o Modelo Desejado:
MCS - Manga Curta simples
MLS - Manga Longa simples
MCE - Manga Curta com estampa
MLE - Manga Longa com estampa
>>""").upper()
        if modelo != "MCS" \
        and modelo != "MLS" \
        and modelo != "MCE" \
        and modelo != "MLE" :
            print("Escolha invalida!, entre com o modelo novamente")
            modelo = None

    # Retorna o valor do modelo com base na escolha do usuário
    if modelo == "MCS":
        return 180
    elif modelo == "MLS":
        return 210
    elif modelo == "MCE":
        return 290
    elif modelo == "MLE":
        return 320
    else:
        return None
    return None

def num_camisetas():
    quantidade_de_camiseta = None

    # Pergunta o número de camisetas;
    # Repete a pergunta se digitar um valor acima de 20000 ou valor não numérico
    # usar try catch
    while not quantidade_de_camiseta:
        quantidade_de_camiseta = input("Entre com a quantidade de camisetas\n>>")
        # Validar valor não numerico
        try:
            quantidade_de_camiseta = int(quantidade_de_camiseta)
        except Exception:
            print("Valor Invalido!")
            quantidade_de_camiseta = None
            continue
        # Limite de quantidade
        if quantidade_de_camiseta > 20000:
            print("Não é aceito pedidos nessa quantidade de camisetas!")
            quantidade_de_camiseta = None
            continue

    #Retorna o número de camisetas com desconto
    if quantidade_de_camiseta < 20:
        return int(( (100 - 0) * quantidade_de_camiseta ) / 100)
    elif quantidade_de_camiseta >= 20 and quantidade_de_camiseta < 200:
        return int(( (100 - 5) * quantidade_de_camiseta ) / 100)
    elif quantidade_de_camiseta >= 200 and quantidade_de_camiseta < 2000:
        return int(( (100 - 7) * quantidade_de_camiseta ) / 100)
    elif quantidade_de_camiseta >= 2000 and quantidade_de_camiseta <= 20000:
        return int(( (100 - 12) * quantidade_de_camiseta ) / 100)

    return None

def frete():
    tipo_de_frete = None

    #Pergunta pelo serviço adicional de frete
    #Repetir a pergunta item. se digitar uma opção diferente de: 1/2/0;
    while not tipo_de_frete:
        tipo_de_frete = input("""
Escolha o tipo de frete:
1 - Frete por transportadora - R$ 100.00
2 - Frete por sedex - R$ 200.00
0 - Retirar na fabrica - R$ 0.00
>>""")
        # Validar valor não numerico
        try:
            tipo_de_frete = int(tipo_de_frete)
        except Exception:
            print("Valor Invalido!")
            tipo_de_frete = None
            continue
        if tipo_de_frete != 1 \
        and tipo_de_frete != 2 \
        and tipo_de_frete != 0:
            print("Escolha invalida!, entre com o tipo de frete novamente")
            tipo_de_frete = None

    #Retorna o valor das opções de frete
    if tipo_de_frete == 1:
        return 10000
    elif tipo_de_frete == 2:
        return 20000
    elif tipo_de_frete == 0:
        return 0
    return None

def main():
    # Cobrança de serviços de uma fábrica que vende Camisetas em atacado.

    # Dados
    valor_do_modelo_da_camiseta = None
    quantidade_de_camiseta = None
    valor_do_tipo_de_frete = None
    total_a_pagar = None

    print("Bem Vindo ao Estabelecimento do Vinicius Eduardo Carvalho da Cruz de Moura")
    
    # Rotinas
    valor_do_modelo_da_camiseta = escolha_modelo()
    quantidade_de_camiseta = num_camisetas()
    valor_do_tipo_de_frete = frete()
    total_a_pagar = valor_do_modelo_da_camiseta * quantidade_de_camiseta + valor_do_tipo_de_frete

    # Saida dos Valores 
    print("Total", "R$", "{0:.2f}".format(total_a_pagar/100), "(Modelo :", "{0:.2f}".format(valor_do_modelo_da_camiseta/100), "* Quantidade(com desconto): ", quantidade_de_camiseta ,"+ frete:", "{0:.2f}".format(valor_do_tipo_de_frete/100), ")")
    
if __name__ == '__main__':
    main()
