def rail_fence(check, type, key, sentence):
    # check should be either 'e' for encryption or 'd' for decryption
    # type should be either 't' for text input or 'r' for reading from file
    # key is the integer number of rails in the rail fence cipher
    # sentence is the string of text to be encrypted or decrypted

    # initialize variables
    x = 0
    y = 0
    step = 1
    check_no = 0
    no = 0
    check_list = []
    original_list = []
    main_logic = 0
    new_list = []
    number = 0
    check_logic = 1
    constant = 2

    # read from file if type is 'r'
    if type == "r":
        with open("Rail_fence_cipher.txt", "r") as f:
            sentence = f.read()

    # get length of sentence
    length = len(sentence)

    # clear contents of file
    with open("Rail_fence_cipher.txt", "w") as f:
        f.write("")

    # encryption
    if check == "e":
        # store original characters in original_list
        while no != length:
            original_list.append(sentence[no])
            no += 1

        # create check_list to store positions of characters in the rail fence
        while check_no != length:
            if (step == 1 and y == key-1) or (step == -1 and y == 0):
                step *= -1
            x = check_no
            check_list.insert(x, [x, y])
            y += step
            check_no += 1

        # create new_list by adding original characters to their corresponding positions in the rail fence
        check_no = 0
        while main_logic != key:
            x = 0
            while x != length:
                if check_list[x][1] == check_no:
                    new_list.append(original_list[x])
                x += 1
            main_logic += 1
            check_no += 1

    # decryption
    if check == "d":
        de_list = [0 for col in range(length)]

        # first line placement of characters in the list
        x = (length - 1) // (2*(key)-2)+2
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

        # placement of characters in the list
        while check_no != length:
            if x == 0:
                no = no + 2*(key)-2
                de_list[no] = sentence[check_no]
                check_list.append(no)
                check_no += 1
                x = 1
            else:
                no = no + 2*(key)-2
                de_list[no] = sentence[check_no]
                check_list.append(no)
                check_no += 1
                x = 0
            if check_no == length:
                break
            if step == 1:
                no = no - 2*(key)-2
                de_list[no] = sentence[check_no]
                check_list.append(no)
                check_no += 1
                step += 1
            else:
                no = no + 2*(key)-2
                de_list[no] = sentence[check_no]
                check_list.append(no)
                check_no += 1
                step -= 1
        check_no = 0
        while check_no != length:
            new_list.append(de_list[check_list[check_no]])
            check_no += 1

        # write to file
        with open("Rail_fence_cipher.txt", "a") as f:
            for x in new_list:
                f.write(x)

        # print to console
        print("".join(new_list))

# main function


def main():
    # get input from user
    check = input("Enter 'e' for encryption or 'd' for decryption: ")
    type = input("Enter 't' for text input or 'r' for reading from file: ")
    key = int(input("Enter the number of rails: "))
    sentence = input("Enter the text to be encrypted or decrypted: ")

    # call rail_fence function
    rail_fence(check, type, key, sentence)


# call main function
main()
