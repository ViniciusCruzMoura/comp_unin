package cofre;

import java.util.Scanner;

public class Main {

    public static void show_main_menu() {
        System.out.println("Menu");
        System.out.println("1-Adicionar");
        System.out.println("2-Remover");
        System.out.println("3-Listar");
        System.out.println("4-Calcular Total em Reais");
        System.out.println("0-Encerrar");
    }

    public static void show_coins_types() {
        System.out.println("Tipos de Moedas");
        System.out.println("1-Real");
        System.out.println("2-Euro");
        System.out.println("3-Dolar");
    }

    public static void main(String[] args) {
        boolean should_close = false;
        Scanner input = new Scanner(System.in);
        int option_selected;
        Cofrinho piggy_bank = new Cofrinho();
        int coin_type_selected;
        double monetary_value;
        Moeda money;

        show_main_menu();
        option_selected = input.nextInt();

        while (option_selected != 0) {
            switch(option_selected) {
                // Fluxo de execução para a Opção de Adição de nova Moeda
                // no Cofrinho
                case 1:
                    System.out.println("Adicionar moedas de diferentes valores e paises em seu cofrinho.");

                    // Seleção de tipo de moeda
                    coin_type_selected = 0;
                    while (coin_type_selected > 3 || coin_type_selected <= 0) {
                        show_coins_types();
                        coin_type_selected = input.nextInt();
                    }

                    // Pegar Valor da Moeda
                    System.out.println("Qual e o valor monetario?");
                    monetary_value = input.nextDouble();

                    // Instanciar Tipo de Moeda com o valor inserido
                    money = null;
                    if (coin_type_selected == 1) {
                        money = new Real(monetary_value);
                    } else if (coin_type_selected == 2) {
                        money = new Euro(monetary_value);
                    } else {
                        money = new Dolar(monetary_value);
                    }
                    
                    // Adiciona a Moeda na lista
                    piggy_bank.adicionar(money);
                    break;
                // Fluxo de execução para a Opção de Remoção de Moeda
                // no Cofrinho
                case 2:
                    System.out.println("Remover moedas especificas do cofrinho.");

                    // Seleção de tipo de moeda
                    coin_type_selected = 0;
                    while (coin_type_selected > 3 || coin_type_selected <= 0) {
                        show_coins_types();
                        coin_type_selected = input.nextInt();
                    }

                    // Pegar Valor da Moeda
                    System.out.println("Qual e o valor monetario?");
                    monetary_value = input.nextDouble();

                    money = null;
                    if (coin_type_selected == 1) {
                        money = new Real(monetary_value);
                    } else if (coin_type_selected == 2) {
                        money = new Euro(monetary_value);
                    } else {
                        money = new Dolar(monetary_value);
                    }

                    // Remove a Moeda da lista
                    piggy_bank.remover(money);
                    break;
                // Fluxo de execução para a Opção de Listagem de Moedas
                // no Cofrinho
                case 3:
                    System.out.println("Listar todas as moedas que estao dentro do cofrinho");
                    piggy_bank.listagemMoedas();
                    break;
                // Fluxo de execução para a Opção de Total de Moedas
                // no Cofrinho
                case 4:
                    System.out.println("Calcular quanto dinheiro existe no cofrinho convertido para Real");
                    System.out.println("Total Convertido para Reais: " + piggy_bank.totalConvertido());
                    break;
                // Fluxo de execução para a Opção de Invalida
                default:
                    System.out.println("Opcao invalida!");
            }
            show_main_menu();
            option_selected = input.nextInt();
        }
    }
}

