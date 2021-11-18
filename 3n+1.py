from datetime import datetime
from time import sleep
from colorama import Fore, init, Style
init(autoreset=True)


# GLOBAL SWITCHES

attempt_count: int = 0
highest: int = 0
seed_value: int = 0
starting_time = datetime.now()

PRINT_NUMBERS: bool = False  # Recommended to set false when testing huge numbers
SLOW_PRINT: bool = False


def getDuration():
    global starting_time
    return (datetime.now() - starting_time)


def resetTimer():
    global starting_time
    starting_time = datetime.now()


def conjecture(num: int):

    global attempt_count
    global highest
    global seed_value

    attempt_count = attempt_count + 1
    if(SLOW_PRINT):
        sleep(0.1)

    if (num > highest):
        highest = num

    if (num % 2 != 0):  # if Odd

        if (PRINT_NUMBERS):
            print(Fore.CYAN + str(int(num)) + Style.RESET_ALL)

        new_num: int = (3 * num) + 1
    else:

        if(PRINT_NUMBERS):
            print(Fore.BLUE + str(int(num)) + Style.RESET_ALL)

        new_num: int = (num // 2)

    if (num != 1.0):

        # if (new_num > highest):
        #     highest = new_num
        return new_num

    else:
        print(f"""
-----

Collatz conjecture encountered after {Fore.MAGENTA }{attempt_count - 3 if attempt_count > 3 else 0}{Style.RESET_ALL} attempts! 
Execution time: {Fore.CYAN}{getDuration()}{Style.RESET_ALL}
Seed {Fore.CYAN}[{len(str(seed_value))}]{Style.RESET_ALL}: {Fore.RED}{seed_value}{Style.RESET_ALL}
Highest {Fore.CYAN}[{len(str(highest))}]{Style.RESET_ALL}: {Fore.YELLOW}{highest}{Style.RESET_ALL}
Increased {Fore.CYAN}[{len(str(highest - seed_value))}]{Style.RESET_ALL}: {Fore.BLUE}{highest - seed_value}{Style.RESET_ALL}

        """)
        attempt_count = 0
        highest = 0
        seed_value = 0

        return "halt"


def main_loop(output_value):  # initial input is also called output_value for lack of coffee
    resetTimer()
    print("-----\n")
    while True:
        if (output_value == "halt"):
            break
        output_value = conjecture(output_value)


while True:
    seed_value = int(input("Enter seed number [except 1]: "))
    main_loop(seed_value)
