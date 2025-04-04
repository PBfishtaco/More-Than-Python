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
    else:
        print("word:", letters, sep="")
    letters = list(letters)
    for i in range(len(letters)):
        letters[i] = chr(ord(letters[i]) + number)
    print("".join(letters))
    print("")