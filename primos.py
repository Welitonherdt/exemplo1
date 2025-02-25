# Função para verificar se o número é primo
def verificar_primo(num):
    if num < 2:  # 1 e números negativos não são primos
        return False
    for i in range(2, num):
        if num % i == 0:  # Se for divisível por outro número que não seja 1 ou ele mesmo
            return False
    return True


# Função principal
def main():
    # Solicitar que o usuário insira um número para verificar
    num = int(input("Informe o numero para verificar se é primo: "))

    # Chama a função e imprime o resultado
    if verificar_primo(num):
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")


# Chamando a função principal
if __name__ == "__main__":
    main()