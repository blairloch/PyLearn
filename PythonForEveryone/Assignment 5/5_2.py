largest_num = None
smallest_num = None
while True :
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        ival = int(sval)
    except:
        print("Invalid input")
        continue
    if smallest_num is None :
        smallest_num = ival
    elif ival < smallest_num :
        smallest_num = ival
    if largest_num is None :
        largest_num = ival
    elif ival > largest_num :
        largest_num = ival

print("Maximum is", largest_num)
print("Minimum is", smallest_num)




 