def rail_fence_cipher(encrypt_or_decrypt: str, input_type: str, key: int, sentence: str = None) -> str:
    if input_type == "t":
        sentence = input("Sentence: ")
    elif input_type == "r":
        with open("Rail_fence_cipher.txt", "r") as f:
            sentence = f.read()

    length = len(sentence)
    if encrypt_or_decrypt == "e":
        encrypted = ["" for _ in range(key)]
        row, direction = 0, 1
        for char in sentence:
            encrypted[row] += char
            row += direction
            if row == key - 1:
                direction = -1
            elif row == 0:
                direction = 1
        return "".join(encrypted)
    elif encrypt_or_decrypt == "d":
        rows = ['' for _ in range(key)]
        row, direction, index = 0, 1, 0
        for char in sentence:
            rows[row] += char
            row += direction
            if row == key - 1:
                direction = -1
            elif row == 0:
                direction = 1
        return "".join(rows)


encrypt_or_decrypt = input("Encrypt or decrypt ('e' or 'd') : ").lower()
input_type = input(
    "Input *t* or *r* to tyep or read from text file : ").lower()
key = int(input("Enter the key : "))
while key <= 1:
    print("Invalid key")
    key = int(input("Re-enter the key : "))

result = rail_fence_cipher(encrypt_or_decrypt, input_type, key)
print(result)

with open("Rail_fence_cipher.txt", "w") as f:
    f.write(result)
