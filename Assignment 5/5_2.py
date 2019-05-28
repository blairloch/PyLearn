largest_num = None
smallest_num = None
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = int(sval)
    except:
        print("Invalid input")
        continue
    if smallest_num is None :
        smallest_num = fval
    elif fval < smallest_num :
        smallest_num = fval
    if largest_num is None :
        largest_num = fval
    elif fval > largest_num :
        largest_num = fval

print("Maximum is", largest_num)
print("Minimum is", smallest_num)




 