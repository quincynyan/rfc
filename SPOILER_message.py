check = str(input("Encrypt or decrypt ('e' or 'd') : "))
check = check.lower()
type = str(input("Input *t* or *r* to tyep or read from text file : "))
type = type.lower()

key = int(input("Enter the key : "))
while key <= 1:
    print("Invalid key")
    key = int(input("Re-enter the key : "))
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


if type == "t":
    sentence = str(input("Sentnce : "))
elif type == "r":
    a = open("Rail_fence_cipher.txt", "r")
    sentence = a.read()
    a.close()
length = len(sentence)


# clearing the text file
a = open("Rail_fence_cipher.txt", "w")
a.write("")
a.close()

# Encryption
if check == "e":
    while no != length:
        original_list.append(sentence[no])
        no += 1
    while check_no != length:
        if (step == 1 and y == key-1) or (step == -1 and y == 0):
            step *= -1
        x = check_no
        check_list.insert(x, [x, y])
        y += step
        check_no += 1

    check_no = 0
    while main_logic != key:
        x = 0
        while x != length:
            if check_list[x][1] == check_no:
                new_list.append(original_list[x])
            x += 1
        main_logic += 1
        check_no += 1

# Decryption
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
    # Placement for character in the middle
    while step != key:
        x += 1
        y = x
        de_list[y] = sentence[check_no]
        check_no += 1
        check_logic = 1
        while (y + (2*key)-2-constant <= length-1 and check_logic == 1) or (y + constant <= length - 1 and check_logic == -1):
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

    y = (2*key)-2
    number = int(y/2)
    de_list[number] = sentence[check_no]
    check_no += 1
    for x in sentence[check_no:length]:
        number += y
        de_list[number] = x
    new_list = de_list

for i in range(len(new_list)):
    print(new_list[i], end="")
    a = open("Rail_fence_cipher.txt", "a")
    a.write(new_list[i])
    a.close()
