def valid_password(password):
    if True==True:
        
        s=['&', '*','%','$','#','!','?']    
        if  len(password)<8:
            print('password is less than 8 characters')
        
            #checks that pass is at least 8 characters
        if  not any(password.isupper() for password in password):
            print("password needs an upper case")
    
            # check for upper case
        if not any(password.isdigit()for password in password):
            print("password needs a number")
    
            #check for a number
        if not any(password.islower() for password in password):
            print("password needs a lowercase letter")
    
            #checks for lowercase
        if not any(password in s for password in password):
            print("you need a symbol")
    
        # checks for symbol
        
        else:
            print("password is valid")
        
print(valid_password("jkjkjkjse9!G"))