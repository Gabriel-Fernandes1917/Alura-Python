print("Welcome to my game")

secret_number = 42
total_attempts = 3
attempts = 1

while(attempts <= total_attempts):
    ##.format is String interpolation
    print("You have {} attemps the {}".format(attempts, total_attempts))
    chute_str = input("Digite your number: ")

    print("You write ", chute_str)

    chute = int(chute_str)   
    ## add conditions in variables
    correct = secret_number == chute

    taller = chute > secret_number

    smaller = chute < secret_number

    if(correct):
        print("All right !!!")
        attempts = 40
    else:
        if(taller):
            print("You lose ! Your choise is taller than secret number")
        elif(smaller):
            print("You lose ! Your choise is samller than secret number")
    attempts = attempts+1

print("GAME OVER")