print("\n\nIniciando a aplicação, siga as instruções:")


def medias(val1, val2, val3, char):
    if char == 'A' or char == 'a':
      return (val1 + val2 + val3) / 3
    elif char == 'P' or char == 'p':
        return (val1*5) + (val2*3) + (val3*2) / (5 + 3 + 2)
    elif char == 'H' or char == "h":
        return 3 / (1/val1) + (1/val2) + (1/val3)

while True:
        pergunta1 = float(input("Qual é o primeiro valor? "))
        pergunta2 = float(input("Qual é o segundo valor? "))
        pergunta3 = float(input("Qual é o terceiro valor? "))
        pergunta4 = str(input("Qual é o tipo de média (A, P or H? "))

        resposta = medias(pergunta1, pergunta2, pergunta3, pergunta4)

        print("O resultado da média é:", resposta)

        repeat = str(input("Deseja realizar um novo cálculo (S or N)? "))

        if repeat == "N" or repeat == "n":
            exit()

        print("\n\nReiniciando a aplicação:\n")