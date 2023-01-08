import re


def rail_fence_cipher(operation, input_type, key, sentence=''):
    """
    Perform rail fence cipher encryption or decryption on the given input.

    Parameters:
    operation (str): 'e' for encryption, 'd' for decryption.
    input_type (str): 't' for typed input, 'r' for input from file.
    key (int): Key for the cipher. Must be greater than 1.
    sentence (str, optional): Sentence to encrypt or decrypt. Required if input_type is 't', ignored if input_type is 'r'.

    Returns:
    str: Encrypted or decrypted sentence.
    """
    # Ensure operation is lowercase
    operation = operation.lower()
    # Ensure input type is lowercase
    input_type = input_type.lower()
    # Ensure key is valid
    while key <= 1:
        print("Invalid key. Re-enter key: ")
        key = int(input())

    # Read input from file or user
    if input_type == 'r':
        with open("Rail_fence_cipher.txt", "r") as f:
            sentence = f.read()
    elif input_type == 't':
        # Ensure input is not empty
        while not sentence:
            print("Sentence cannot be empty. Enter sentence: ")
            sentence = input()

    # Initialize variables
    length = len(sentence)
    original_list = []
    check_list = []
    new_list = []

    # Encryption
    if operation == 'e':
        # Create list of original characters
        for i in range(length):
            original_list.append(sentence[i])
        # Create list of positions for each character in the encrypted sentence
        x = 0
        y = 0
        step = 1
        for i in range(length):
            if (step == 1 and y == key-1) or (step == -1 and y == 0):
                step *= -1
            check_list.append([x, y])
            x += 1
            y += step
        # Create encrypted sentence
        for i in range(key):
            for j in range(length):
                if check_list[j][1] == i:
                    new_list.append(original_list[j])

    # Decryption
    elif operation == 'd':
        de_list = [0 for _ in range(length)]

        # Placement of characters in first row of de_list
        x = (length - 1) // (2*(key)-2)+2
        for y in range(1, x):
            de_list[(2*(key)-2)*(y-1)] = sentence[y-1]
        # Placement of characters in last row of de_list
        for y in range(1, x):
            de_list[(2*(key)-2)*(y-1)+(key-1)] = sentence[x+y-2]
        # Placement of characters in middle rows of de_list
        for i in range(1, key-1):
            for y in range(1, x):
                de_list[(2*(key)-2)*(y-1)+i] = sentence[x*2+y+i-3]
                de_list[(2*(key)-2)*(y-1)+(key-1)+i] = sentence[x*2+y+i+key-3]
        # Create decrypted sentence
        for i in range(length):
            new_list.append(de_list[i])

    # Return encrypted or decrypted sentence
    return ''.join(new_list)


def main():
    # Get operation
    print("Enter 'e' for encryption or 'd' for decryption: ")
    operation = input()
    # Ensure operation is valid
    while operation.lower() not in ['e', 'd']:
        print("Invalid operation. Enter 'e' for encryption or 'd' for decryption: ")
        operation = input()

    # Get input type
    print("Enter 't' for typed input or 'r' for input from file: ")
    input_type = input()
    # Ensure input type is valid
    while input_type.lower() not in ['t', 'r']:
        print("Invalid input type. Enter 't' for typed input or 'r' for input from file: ")
        input_type = input()

    # Get key
    print("Enter key: ")
    key = int(input())

    # Get sentence
    sentence = ''
    if input_type == 't':
        print("Enter sentence: ")
        sentence = input()

    # Perform rail fence cipher
    output = rail_fence_cipher(operation, input_type, key, sentence)

    # Print output
    print(output)

    # Write output to file
    with open("Rail_fence_cipher.txt", "w") as f:
        f.write(output)


if __name__ == "__main__":
    main()
