userInput = input("Please enter in the range(s) you want printed: ")

stringStart = ""
stringEnd = ""


for x in userInput:
    if x is "-":
        stringStart = userInput[0:x.index]
        stringEnd = userInput[x.index:userInput.index(" ")]

        n = int(stringStart)
        while n < int(stringEnd):
            print(n)
            n += 1

        userInput.remove(stringStart + "-" + stringEnd)
               