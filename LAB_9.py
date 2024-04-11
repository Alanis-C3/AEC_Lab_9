# Lab 9 for cop3052
# collaborative lab
# Student : Alanis Castillo


def main_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")
    option = input("Please enter an option: ")
    return option



def encode(password):
    encode_pwd = []
    for i in range(0, len(password)):
        new_num = int(password[i]) + 3  # adding 3 to each element in the password
        if new_num > 9:
            new_num = new_num % 10  # in case when add 3 is > 9 it will add only 2nd num
        encode_pwd.append(str(new_num))  # adds new number to list
    return "".join(encode_pwd)  # coverts list of new numbers into a string

if __name__ == "__main__":
    option = 0
    while option != "3":
        option = main_menu()
        if option == "1":
            password = input("Please enter your password to encode: ")
            current_pwd = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            orginal_pwd = 0
            print(f"The encoded password is {current_pwd}, and the original password is {orginal_pwd}")
        elif option == "3":
            break
