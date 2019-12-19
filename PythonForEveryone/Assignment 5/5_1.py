num = 0
tot = 0.0 
print("Please use this programme to input a list of numbers, when finished please respond to the prompt with done")
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("Invalid Input")
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print("All Done")
print("Total: ", tot, " Count: ", num, " Average: ",tot/num)
