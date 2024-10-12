import time
from os import system, name

while True:
    choice = input("Do you want to start? (y/n): ")
    if "y" in choice.lower():
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        total = (hours * 3600) + (minutes * 60) + seconds
        print("Timer starts now...")
        time.sleep(1)
        while total >= 1:
            print(total)
            total -= 1
            time.sleep(1)
            if name == "nt":
                system("cls")
            else:
                system("clear")
        print("Timer ended :)")
    elif "n" in choice.lower():
        print("Exiting...")
        break
    else:
        print("Your choice is wrong! :(")
