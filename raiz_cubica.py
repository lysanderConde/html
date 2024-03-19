def calcular_raiz_cubica(numero):
    raiz = numero ** (1/3)
    if raiz <= 10:
        print("Não é necessário o uso de calculadora.")
    else:
        print("É necessário o uso de calculadora.")
if __name__ == "__main__":
    entrada = float(input("Digite um número para calcular a raiz cúbica: "))
    calcular_raiz_cubica(entrada)