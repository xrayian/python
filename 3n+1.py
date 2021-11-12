from datetime import datetime

incarnations:int = 0
highest:int = 0
starting_time = datetime.now()


def getDuration():
    global starting_time
    return (datetime.now() - starting_time)

def resetTimer():
    global starting_time
    starting_time = datetime.now()


def conjecture(num:int):

    global incarnations
    global highest
    
    incarnations = incarnations + 1
    
    if (num > highest):
            highest = num
    
    
    if (num % 2 != 0): #if Odd
        print(int(num))
        new_num:int = (3 * num) + 1
    else :
        print(int(num))
        new_num:int = (num // 2)
    
    if (num != 1.0):
        # if (new_num > highest):
        #     highest = new_num
        return new_num
    else:
        print(f"-----\nCollatz conjecture encountered after {incarnations} attempts [highest: {highest}, took {getDuration()}s]\n")
        incarnations = 0
        highest = 0
        return "halt"



def main_loop(output_value): #initial input is also called output_value for lack of coffee
    resetTimer()
    print("-----")
    while True:
        if (output_value == "halt"):
            break
        output_value = conjecture(output_value)

while True:
    main_loop(int(input("Enter a number [except 1]: ")))
    