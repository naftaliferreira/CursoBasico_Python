# Ask the user to enter a number. If it is under 10, display the mensage: "Too low", if their number is between 10 and 20
# Display "Correct", orherwise display "Too high".

number = int(input("Insert a number between 10 and 20 here: "))
if number > 10 and number < 20:
    print("Correct")
elif number < 10:
    print("Too low!")
else:
    print("Too high!")

# Código funcionando corretamente, sintaxes simples e funcionais.
