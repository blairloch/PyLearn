def langgreeting(lang):
    if lang == 'es':
        return ('Hola, I see you want to use Spanish')
    elif lang == 'fr':
        return ('Bonjour, I see you want to use French')
    elif lang=='eng':
        return ('Hello, I see you want to use English')
    else :
        return ("Sorry, I don't understand that language")

lang1 = input('What Language do you want to run this programme under? ')
print(langgreeting(lang1))
lang2 = input("And What about the second user? ")
print(langgreeting(lang2) , "I am glad there are two users")