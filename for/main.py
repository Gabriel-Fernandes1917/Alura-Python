print("Welcome to my game")

secret_number = 42
total_attempts = 3
attempts = 1

for attempts in range (1, total_attempts+1):
    ##.format is String interpolation
    print("You have {} attemps the {}".format(attempts, total_attempts))
    chute_str = input("Digite one number between 1 and 100: ")

    print("You write ", chute_str)

    chute = int(chute_str)   
    ## add conditions in variables
    small1 = chute < 1
    taller100 = chute > 100
    if(small1 or taller100):
        print("you need write one number between 1 and 100: ")
        continue ## continue return to loop he not break loop

    correct = secret_number == chute

    taller = chute > secret_number

    smaller = chute < secret_number



    if(correct):
        print("All right !!!")
        break ## exit loop
    else:
        if(taller):
            print("You lose ! Your choise is taller than secret number")
        elif(smaller):
            print("You lose ! Your choise is samller than secret number")
    

print("GAME OVER")