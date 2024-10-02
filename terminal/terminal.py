import sys
import os
from datetime import datetime


def terminal():
    print("Welcome to the terminal.")
    print('Type "help" for the list of commands')

    while True:
        userInput = input("~> ")

        if userInput == "exit":
            print("Exiting...")
            break

        elif userInput == "help":
            with open("terminal/help.txt", "r") as file:
                print(file.read())

        elif userInput == "list":
            if sys.platform == "darwin" or sys.platform == "linux":
                os.system("ls -l")
            else:
                os.system("dir")

        elif userInput == "time":
            time = datetime.now().strftime("%H:%M:%S")
            print(time)

        elif userInput == "date":
            date = datetime.today().strftime("%B %d, %Y")
            print(date)

        elif userInput == "version":
            print("1.0.0")

        else:
            print('Unknown command. Please refer to the "help" command.')


if __name__ == "__main__":
    terminal()
