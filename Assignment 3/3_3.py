score = input('Please enter the score between 0 & 1 ')
try:
    score = float(score)
except:
    print("Error, Please enter a number between 0 & 1")
    quit()    
    
if score < 0 :
    print("Error, Please enter a number between 0 & 1 ")
elif score > 1 :
    print("Error, Please enter a number between 0 & 1 ")
elif score >= 0.9 :
    print ('A')
elif score >= 0.8 :
    print ('B')
elif score >= 0.7 :
    print ('C')
elif score >= 0.6 :
    print ('D')
else:
    print('F')



