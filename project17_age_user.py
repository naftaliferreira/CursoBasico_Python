# perguntar ao usuário qual é a idade dele, caso ele tenha mais de 18 anos, responda: "You can vote".
# caso o usuário tenha 17 anos de idade, responda: "You can learn to drive".
# Caso o usuário tenha 16 anos de idade, responda: "You can buy a lottery ticket".
# Caso o usuário tenha menos de 16 anos de idade, responda: "You can go Trick-or-Treating".

age_of_user = int(input("What's your age? "))
if age_of_user >= 18:
    print("You can vote!")
elif age_of_user >= 17:
    print("You can learn drive!")
elif age_of_user >= 16:
    print("You can buy a lottery ticket!")
else:
    print("You can go Trick-on-Treating")

# Código útil e funcional
