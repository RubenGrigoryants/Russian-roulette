import random
import time 
import os
import sys

def main():
    bullet = 6
    random_bullet = random.randrange(1,6)
    while(True):
        c = input("\n1 = стрелять . 2 = сдаться\n")
        os.system('cls||clear')
        if c == "1":
            if bullet == random_bullet:
                print("Смерть")
                sys.exit()
            else:
                bullet -= 1
                print(bullet)
        if c == "2":
            print(f"патрон был в {random_bullet} ")
            sys.exit()
    
    

main()

