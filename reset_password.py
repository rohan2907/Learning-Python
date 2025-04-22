# Need to reset the password

new_pass = input("New Password: ")
conf_pass = input("Confirm Password: ")

if new_pass == conf_pass:
    print("Password Changed")   
elif new_pass.casefold() == conf_pass.casefold():
    print("Please check cases and try again")
else:
    print("Password do not match, try again!!")            
        
