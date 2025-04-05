import pyperclip
kill = False
while True:
    while True:
        if kill == True:
            exit()
        try:
            number = input("Number: ")
            if number == "":
                kill = True
            number = int(number)
            letters = input("Text: ")
        except:
            print("err\n")
        else:
            break
    if letters == "":
        exit()
    letters = list(letters)
    for i in range(len(letters)):
        letters[i] = chr(ord(letters[i]) + number)
    letters = "".join(letters)
    print(letters)
    try:
        if input("Copy to clipboard?: ")[0].lower() == "y":
            pyperclip.copy(letters)
    except:
        pass
    print("")