# Pedir ao usuário para inserir sua cor favorita, caso ele escolha o "vermelho" exibir a mensagem, eu tambem.
# Caso o usuário responda outra cor, retorne a mensagem: "Eu não gosto de [cor], prefiro vermelho"

colour = input("What's your favorite color?  ")
if colour == "red" or colour == "Red" or colour == "RED":
    print("Cool, red is my favorite color too.")
else:
    print("I don't like", colour, "I prefer red")

# Código funcionando corretamente!
