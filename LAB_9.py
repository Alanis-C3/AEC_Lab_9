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


def decode_password(encoded_password):
    constant_value = 3  # Making sure each digit gets shifted down by 3 numbers
    original_password = []  # Creating empty list to store original password
    for digit in encoded_password:
        original_digit = str((int(digit) - constant_value + 10) % 10)  # Subtract 3 from each digit
        original_password.append(original_digit)
    return ''.join(original_password)  # returning the original password



if __name__ == "__main__":
    option = 0  # dummy variable for while loop
    while option != "3":  # while loop for when option is not equal to 3
        option = main_menu()
        if option == "1":  # if user picks option 1, encode the original password
            password = input("Please enter your password to encode: ")
            current_pwd = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":  # if user picks option 2, decode the encoded password
            orginal_pwd = decode_password(current_pwd)
            print(f"The encoded password is {current_pwd}, and the original password is {orginal_pwd}.\n")
        elif option == "3":  # if user picks option 3, break
            break
