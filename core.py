from datetime import datetime
from time import sleep
import sys, getopt
from colorama import Fore, init, Style
init(autoreset=True)

print_numbers: bool = True
print_dots: bool = False
slow_print: bool = False


# GLOBAL SWITCHES

attempt_count: int = 0
highest: int = 0
seed_value: int = 0
starting_time = datetime.now()

def print_outputs(fast_mode: bool = True):
    global print_numbers
    print_numbers = fast_mode

def slow_print_numbers(slow_mode: bool = False):
    global slow_print
    slow_print = slow_mode

def ball_mode(ball_mode: bool = False):
    global print_dots
    print_outputs(False)
    print_dots = ball_mode


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
    
    if((print_numbers or print_dots) and slow_print): sleep(0.1)

    if (num > highest): highest = num
    
    if (num % 2 != 0):  # if Odd
        if (print_numbers): print(Fore.CYAN + str(int(num)) + Style.RESET_ALL)
        if (print_dots): print(Fore.CYAN + "•"*int(num) + Style.RESET_ALL)
        new_num: int = (3 * num) + 1
    
    else:
        if(print_numbers): print(Fore.BLUE + str(int(num)) + Style.RESET_ALL)
        if (print_dots): print(Fore.BLUE + "•"*int(num) + Style.RESET_ALL)

        new_num: int = (num // 2)

    if (num != 1.0): return new_num

    else:
        if print_numbers or print_dots: print("-----\n")
        print(f"""
Collatz conjecture encountered after {Fore.MAGENTA }{attempt_count - 3 if attempt_count > 3 else 0}{Style.RESET_ALL} attempts! 
Execution time: {Fore.CYAN}{getDuration()}{Style.RESET_ALL} { "" if (print_outputs) else "FAST MODE"}
Seed {Fore.CYAN}[{len(str(seed_value))}]{Style.RESET_ALL}: {Fore.RED}{seed_value}{Style.RESET_ALL}
Highest {Fore.CYAN}[{len(str(highest))}]{Style.RESET_ALL}: {Fore.YELLOW}{highest}{Style.RESET_ALL}
Increased {Fore.CYAN}[{len(str(highest - seed_value))}]{Style.RESET_ALL}: {Fore.BLUE}{highest - seed_value}{Style.RESET_ALL}

        """)
        reset()
        return "halt"


def main_loop(initial_seed):
    global seed_value
    
    seed_value = initial_seed
    looping_seed = initial_seed
    
    resetTimer()
    
    if print_numbers or print_dots: print("-----")
    
    while True:
        if (looping_seed == "halt"): break
        looping_seed = conjecture(looping_seed)


def parse_arguments():
    
    def read_file(file_name):
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
    options = "fsbr:"
    long_options = ["fast", "ball-mode", "slow","read="]
    try:
        arguments, values = getopt.getopt(argumentList, options, long_options)
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-f", "--fast"):
                print ("FAST MODE\n")
                print_outputs(False)
            
            if currentArgument in ("-b", "--ball-mode"):
                print ("BALL MODE\n")
                ball_mode(True)
                print_outputs(False)

            if currentArgument in ("-s", "--slow"):
                print ("SLOW MODE\n\n")
                slow_print_numbers(True)

            if currentArgument in ("-r", "--read"):
                read_file(currentValue)

    except getopt.error as err:
        print (str(err))



if __name__ == "__main__":
    
    parse_arguments()

    while True:
        seed_value = input("Enter seed number: ")
        try:
            seed_value = int(seed_value)
            main_loop(seed_value)
        except:
            print(f"{Fore.RED}Invalid Seed! Enter a proper whole integer{Style.RESET_ALL}")
    
