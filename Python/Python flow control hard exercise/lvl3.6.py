#Password Strength Checker

special_characters = "!@#$%^&*()-""+?_=,<>/"
passwd = input('please enter your password: ')
if (len(passwd) < 6 or len(passwd) > 10):
            print('The password needs to be between 6 or 10 characters.')
else:
    count =1
    for i in passwd:
        if i.isupper():
            count += 1
        if (i == special_characters):
            count +=1
        if i.isdigit():
            count +=1
    else:
            print('You neede to enter uppercase, special characters and numbers to the password.')

    if count <= 4:
             print(f'The password is weak.')
    elif count >= 5 and count <= 7:
               print('your password is medium.')
    elif count > 7:
               print('your password is strong!')

    
    
