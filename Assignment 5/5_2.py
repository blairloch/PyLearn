largest_num = None
smallest_num = None
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
    if smallest_num is None :
        smallest_num = fval
    elif fval < smallest_num :
        smallest_num = fval
    if largest_num is None :
        largest_num = fval
    elif fval > largest_num :
        largest_num = fval

print("Smallest Value: ", smallest_num)
print("Largest Value: ", largest_num)




 