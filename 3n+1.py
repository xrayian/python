incarnations:int = 0

def conjecture(num:int):
    global incarnations
    incarnations = incarnations + 1
    if (num % 2 != 0): #if Odd
        print(int(num))
        new_num:int = (3 * num) + 1
    else :
        print(int(num))
        new_num:int = (num // 2)
    
    if (num != 1.0):
        # return new_num
        conjecture(new_num)
    else:
        print(f"\n\nCollatz conjecture encountered after {incarnations}\n")
        incarnations = 0

# def loop(lastNum):
#     if(lastNum != 1):


while True:
    last_number = int(input("Enter a number [except 1]:"))
    conjecture(last_number)
    # loop(last_number)
    # while(last_number != 1.0):
    #     conjecture(last_number)
    