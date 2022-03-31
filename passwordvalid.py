def valid_psd():
   
        low, up, sp, dig = 0, 0, 0, 0
        password = input("Enter your password:")
        if (len(password) >= 4):
            for i in password:
                for wrd in password.split():
                    if(wrd[0].isupper()):
                        up += 1

                    if(i.islower()):
                        low += 1

                    if(i.isdigit()):
                        dig += 1

                    if(i == '@' or i == '$' or i == '_' or i == '#'):
                        sp += 1
                            
        else:
            print('Password Contain Atleast 4 Characters')
        if (low >= 1 and up >= 1 and sp >= 1 and dig >= 1):
           print('Your Password Is Valid')
        else:
            print('Your Password Is Invalid')   
        
valid_psd()

