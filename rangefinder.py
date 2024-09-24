userInput = input("Please enter in the range(s) you want printed: ")

stringStart = ""
stringEnd = ""

userInput = userInput.split(" ")


for i in userInput:
    if "-" in i:
        stringStart = i[0:i.index("-")]
        if " " in i:
            stringEnd = i[i.index("-")+1:i.index(" ")+1]
        else:
            stringEnd = i[i.index("-")+1:len(i)]

        n = int(stringStart)
        while n <= int(stringEnd):
            print(str(n), end=" ")
            n += 1
    else:
        print(i, end=" ")
            