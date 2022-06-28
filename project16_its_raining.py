# Pergunte ao usuário se está chovendo, converta a resposta para minusculo, se ele disser sim, pergunte se esta´
# ventando. se ele responder sim responda: "It is too windy for an umbrella." se ele responder a primeira não :
# responda a ele : "Enjoy your day!"

raining = input("Is it raining? ")
raining = str.lower(raining)
if raining == "yes":
    windy = input("Is it windy? ")
    windy = str.lower(windy)
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day!")

# Código mais complicado até o momento, um espaço errado na sintaxe é capaz de retornar mais de 8 erros diferentes
