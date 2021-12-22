import random

print("Welcome to my game")

##print(int(random.random()*100))

secret_number = int(random.randrange(1, 101)) ## number the 1 100
total_attempts = 0
attempts = 1
points = 100
print(secret_number)

nv = int(input(" 1 - easy \n 2 - normal \n 3 - hard \n"))

if(nv == 1):
    total_attempts = 20
elif(nv == 2):
    total_attempts = 10
else:
    total_attempts = 5

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
        print("All right !!! your did {} points !!!".format(points))
        break ## exit loop
    else:
        if(taller):
            print("You lose ! Your choise is taller than secret number")
        elif(smaller):
            print("You lose ! Your choise is samller than secret number")
        points_loss = abs(secret_number - chute) ## absolute not have negative number
        points = points - points_loss

print("GAME OVER secret number is {}".format(secret_number))