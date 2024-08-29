import json, datetime, sys, os 

#
# ALUNO: Vinicius Eduardo Carvalho da Cruz de Moura
# GIT:
#

"""
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que aceita cartões de
crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior conforme a quantidade de parcelas que o cliente desejar, conforme a listagem
abaixo:

- Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
- Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
- Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
- Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
- Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100)

O valor da parcela é calculado da seguinte maneira:
    valorDaParcela = valorDoPedido∗(1+ juros)/quantidadeParcelas

O valor total parcelado é calculado da seguinte maneira:
    valorTotalParcelado= valorDaParcela∗quantidadeParcelas

Elabore um programa em Python que:
A. Deve-se implementar o print com o seu nome completo (somente print, não usar input aqui).
Por exemplo: print(“Bem-vindos a loja do Bruno Kostiuk”) [EXIGÊNCIA DE CÓDIGO 1 de 6];
B. Deve-se implementar o input do valorDoPedido e da quantidadeParcelas [EXIGÊNCIA DE CÓDIGO 2 de 6];
C. Deve-se implementar o Juros conforme a enunciado acima (obs.: atente-se as condições de menor, igual e maior) [EXIGÊNCIA DE CÓDIGO 3 de 6];
D. Deve-se implementar o valorDaParcela e valorTotalParcelado [EXIGÊNCIA DE CÓDIGO 4 de 6];
E. Deve-se implementar as estruturas if, elif e else (todas elas) [EXIGÊNCIA DE CÓDIGO 5 de 6];
F. Deve-se inserir comentários relevantes no código [EXIGÊNCIA DE CÓDIGO 6 de 6];
G. Deve-se apresentar na saída de console uma mensagem com seu nome completo [EXIGÊNCIA DE SAÍDA DE CONSOLE 1 de 2];
H. Deve-se apresentar na saída de console um parcelamento com Juros (quantidadeParcelas maior ou igual a 4) apresentando o valor da Parcela e o valor Total
Parcelado [EXIGÊNCIA DE SAÍDA DE CONSOLE 2 de 2]

"""

def main():
    print("Bem Vindo a Loja do Vinicius Moura")
    print("Entre com o valor do pedido: 1000.0")
    print("Entre com a quantidade de parcelas: 14")
    print("O valor das parcelas é de: R$ 94.29")
    print("O valor total parcelado é de: R$ 1320.00")

if __name__ == '__main__':
    main()
