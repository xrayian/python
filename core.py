from datetime import datetime
from time import sleep
import sys, getopt
from colorama import Fore, init, Style
init(autoreset=True)

print_numbers: bool = True
# print_dots: bool = False
slow_print: bool = False


# GLOBAL SWITCHES

attempt_count: int = 0
highest: int = 0
seed_value: int = 0
starting_time = datetime.now()

def slowMode(fast_mode: bool = True):
    global print_numbers
    print_numbers = fast_mode

# def ballMode(ball_mode: bool = False):
#     global print_dots
    
#     print_dots = ball_mode


def getDuration():
    global starting_time
    return (datetime.now() - starting_time)


def resetTimer():
    global starting_time
    starting_time = datetime.now()

def reset():
    global attempt_count
    global highest
    global seed_value

    attempt_count = 0
    highest = 0
    seed_value = 0


def conjecture(num: int):

    global attempt_count
    global highest
    global seed_value

    attempt_count = attempt_count + 1
    if(print_numbers and slow_print):
        sleep(0.1)

    if (num > highest):
        highest = num

    if (num % 2 != 0):  # if Odd

        if (print_numbers):
            print(Fore.CYAN + str(int(num)) + Style.RESET_ALL)

        new_num: int = (3 * num) + 1
    else:

        if(print_numbers):
            print(Fore.BLUE + str(int(num)) + Style.RESET_ALL)

        new_num: int = (num // 2)

    if (num != 1.0):

        # if (new_num > highest):
        #     highest = new_num
        return new_num

    else:
        if print_numbers: print("-----\n")
        print(f"""
Collatz conjecture encountered after {Fore.MAGENTA }{attempt_count - 3 if attempt_count > 3 else 0}{Style.RESET_ALL} attempts! 
Execution time: {Fore.CYAN}{getDuration()}{Style.RESET_ALL} { "" if (print_numbers) else "FAST MODE"}
Seed {Fore.CYAN}[{len(str(seed_value))}]{Style.RESET_ALL}: {Fore.RED}{seed_value}{Style.RESET_ALL}
Highest {Fore.CYAN}[{len(str(highest))}]{Style.RESET_ALL}: {Fore.YELLOW}{highest}{Style.RESET_ALL}
Increased {Fore.CYAN}[{len(str(highest - seed_value))}]{Style.RESET_ALL}: {Fore.BLUE}{highest - seed_value}{Style.RESET_ALL}

        """)
        reset()
        return "halt"


def main_loop(output_value):  # initial input is also called output_value for lack of coffee
    global seed_value
    seed_value = output_value
    resetTimer()
    if print_numbers: print("-----\n")
    while True:
        if (output_value == "halt"):
            break
        output_value = conjecture(output_value)


def read_file(file_name):
    global seed_value

    try:
        file = open(file_name)
        for seed in file.readlines():
            try:
                seed_value = int(seed)
                if print_numbers: print(f"{Fore.LIGHTYELLOW_EX}Seed: {seed_value}{Style.RESET_ALL}")
                main_loop(seed_value)
            except ValueError:
                print(f"{Fore.RED}Invalid Seed: {seed}{Style.RESET_ALL}\n")
        exit()

    except OSError as err:
        print(str(err))
        exit()

argumentList = sys.argv[1:]
options = "fsr:"
long_options = ["fast", "slow","read="]
try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-f", "--fast"):
            print ("FAST MODE\n")
            slowMode(False)

        if currentArgument in ("-s", "--slow"):
            print ("SLOW MODE\n\n")
            slow_print: bool = True

        if currentArgument in ("-r", "--read"):
            read_file(currentValue)

except getopt.error as err:
    print (str(err))

if __name__ == "__main__":
    while True:
        seed_value = input("Enter seed number: ")
        try:
            seed_value = int(seed_value)
            main_loop(seed_value)
        except:
            print(f"{Fore.RED}Invalid Seed! Enter a proper whole integer{Style.RESET_ALL}")
    
