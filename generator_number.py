from random import randint

qtd_vezes = int(input("Quantas vezes voce deseja sortear? "))

for c in range (1, qtd_vezes + 1):
    random_numbers = (randint(1, 60), randint(1, 60), randint(1, 60),
                    randint(1, 60), randint(1, 60), randint(1, 60))
    print(f"{c} => {random_numbers}")
