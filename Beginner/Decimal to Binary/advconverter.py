refdict = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def base_converter(number, base):
    if(base == 1):
        print("1"*number)
    else:
        new_num = []
        while(number != 0):
            rem = number % base
            number = number // base
            new_num.append(rem)
        new_num = new_num[::-1]
        if(base <= 36):
            for digit in new_num:
                print(refdict[digit], end="")
            print("")
        else:
            print(str(new_num).strip('[]'))


if __name__ == "__main__":
    number = int(input("Enter number to be converted: "))
    base = int(input("Enter the base for required number system: "))
    if(base > 0):
        print(f"\nNumber in base-10:\t{number}")
        print(f"Number in base-{base}:\t", end="")
        base_converter(number, base)
    else:
        print("Invalid Base for standard positional numeral system.")
