import randomNumbero
import forca

print("select your game")

print("1- forca 2- random number")

game = int(input("what game ?"))

if(game == 1):
    print("game forca")
    forca.play()
elif(game == 2):
    print("radom number")
    randomNumbero.play()
    