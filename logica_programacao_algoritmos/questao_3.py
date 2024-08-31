def escolha_modelo():
    #Pergunta o modelo desejado
    #Retorna o valor do modelo com base na escolha do usuário
    #Repete a pergunta do item. se digitar uma opção diferente de: MCS/MLS/MCE/MLE
    return input("Entre com o modelo desejado")

def num_camisetas():
    #Pergunta o número de camisetas;
    #Retorna (use return) o número de camisetas com desconto seguindo a regra do enunciado (desconto calculado em cima do número de camisetas
    #Repete a pergunta do item. se digitar um valor acima de 20000 ou valor não numérico (use try/except para não numérico
    return input("Entre com a quantidade de camisetas")

def frete():
    #Pergunta pelo serviço adicional de frete
    #Retorna (use return) o valor de apenas uma das opções de frete
    #Repetir a pergunta item. se digitar uma opção diferente de: 1/2/0;
    return input("Escolha o tipo de frete")

def main():
    # Cobrança de serviços de uma fábrica que vende Camisetas em atacado.

    # Dados
    modelo_de_camiseta = None
    quantidade_de_camiseta = None
    tipo_de_frete = None
    total_a_pagar = None

    print("Bem Vindo ao Estabelecimento do Vinicius Eduardo Carvalho da Cruz de Moura")
    
    modelo_de_camiseta = escolha_modelo()
    quantidade_de_camiseta = num_camisetas()
    tipo_de_frete = frete()

    # Saida dos Valores 
    print("Total", "R$", "16040.00", "(Modelo : 1.80 * Quantidade(com desconto): 8800 + frete: 200.00 )")
    
if __name__ == '__main__':
    main()
