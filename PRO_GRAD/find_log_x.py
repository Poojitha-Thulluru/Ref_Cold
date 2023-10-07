## time complexity O(log n) to the base + 1

argument = int(input("Enter an Argument : "))
base = int(input("Enter a base : "))
exponent = 0
if (argument >= base) :
    count = 0
    while (base ** exponent <= argument) :
        count+=1
        exponent += 1
    print("While loop count: ",count)
    print("The log Value is :",exponent-1)
else:
    print(0)