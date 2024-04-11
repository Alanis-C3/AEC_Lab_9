# Lab 9 for cop3052
# collaborative lab
# Student : Alanis Castillo


def main():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit")
    option = input("Please enter an option: ")

def encode(password):
    encode_pwd = []

    for i in range(0, len(password)):
        new_num = int(password[i]) + 3 # adding 3 to each element in the password
        if new_num > 9: # if the new number is a two digit num this statement will modulo 10 to get remainder to be added to the encoded list
            new_num = new_num % 10
        encode_pwd.append(str(new_num)) # adds new number to list
    return "".join(encode_pwd) # coverts list of new numbers into a string


