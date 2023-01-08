import string

# Function to encrypt a given string using the Rail Fence Cipher


def encrypt(sentence, key):
    # Initialize variables for encrypting
    x = 0
    y = 0
    step = 1
    check_no = 0
    no = 0
    check_list = []
    original_list = []
    main_logic = 0
    new_list = []

    # Convert the sentence to a list of characters
    original_list = [char for char in sentence]

    # Generate the check list for the Rail Fence Cipher
    while check_no != len(sentence):
        if (step == 1 and y == key-1) or (step == -1 and y == 0):
            step *= -1
        x = check_no
        check_list.insert(x, [x, y])
        y += step
        check_no += 1

    # Generate the encrypted list using the check list
    check_no = 0
    while main_logic != key:
        x = 0
        while x != len(sentence):
            if check_list[x][1] == check_no:
                new_list.append(original_list[x])
            x += 1
        main_logic += 1
        check_no += 1

    # Return the encrypted list as a string
    return ''.join(new_list)

# Function to decrypt a given string using the Rail Fence Cipher


def decrypt(sentence, key):
    # Initialize variables for decrypting
    de_list = [0 for col in range(len(sentence))]
    x = (len(sentence) - 1) // (2*(key)-2)+2
    check_no = 0
    step = 1
    check_list = []
    new_list = []
    check_logic = 1
    constant = 2

    # Decrypt the first line of the Rail Fence Cipher
    no = 0
    for y in range(1, x):
        if y == 1:
            de_list[0] = sentence[y-1]
            no = 0
            check_list.append(0)
        else:
            no = no + 2*(key)-2
            de_list[no] = sentence[y-1]
            check_list.append(no)
        check_no += 1
    step += 1
    x = 0

    # Decrypt the middle lines of the Rail Fence Cipher
    while step != key:
        x += 1
        y = x
        de_list[y] = sentence[check_no]
        check_no += 1
        check_logic = 1
        while (y + (2*key)-2-constant <= len(sentence)-1 and check_logic == 1) or (y + constant <= len(sentence) - 1 and check_logic == -1):
            check_logic *= -1
            if check_logic == -1:
                y += (2*key)-2 - constant
                de_list[y] = sentence[check_no]
            elif check_logic == 1:
                y += constant
                de_list[y] = sentence[check_no]
            check_no += 1
        step += 1
        constant += 2

    # Return the decrypted list as a string
    return ''.join(str(de_list))

# Main function to run the Rail Fence Cipher


def main():
    # Initialize variables
    sentence = ""
    key = 0
    check = ""
    encrypt_list = []
    decrypt_list = []

    # Ask the user for the sentence to encrypt/decrypt
    sentence = input("Enter the sentence to encrypt/decrypt: ")

    # Ask the user for the key to encrypt/decrypt
    key = int(input("Enter the key: "))

    # Ask the user if they want to encrypt or decrypt
    check = input("Enter 'e' to encrypt or 'd' to decrypt: ")

    # Encrypt the sentence
    if check == "e":
        encrypt_list = encrypt(sentence, key)
        print("The encrypted sentence is: ", encrypt_list)

    # Decrypt the sentence
    elif check == "d":
        decrypt_list = decrypt(sentence, key)
        print("The decrypted sentence is: ", decrypt_list)

    # Invalid input
    else:
        print("Invalid input")


# Run the main function
main()
