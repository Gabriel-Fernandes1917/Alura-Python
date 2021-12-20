print("Welcome to my game")

secret_number = 42

chute_str = input("Digite your number: ")

print("You write ", chute_str)

chute = int(chute_str)

##if(secret_number == chute):
##    print("All right !!!")
##else:
##    if(chute > secret_number):
##        print("You lose ! Your choise is taller than secret number")
##    elif(chute < secret_number):
##        print("You lose ! Your choise is samller than secret number")


## add conditions in variables
correct = secret_number == chute

taller = chute > secret_number

smaller = chute < secret_number

if(correct):
    print("All right !!!")
else:
    if(taller):
        print("You lose ! Your choise is taller than secret number")
    elif(smaller):
        print("You lose ! Your choise is samller than secret number")


print("GAME OVER")