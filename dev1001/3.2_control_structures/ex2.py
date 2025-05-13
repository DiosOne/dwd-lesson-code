# Have variables correct_username = "user123" and correct_password = "password_abc".
correct_username = "user123"
correct_password = "password_abc"
# Ask the user for their entered_username and entered_password (using input()).
user_name= input('Please Enter Your Username: ')
user_pass= input('Please Enter Your Password: ')
# If entered_username matches correct_username AND entered_password matches correct_password, print "Login successful!".
if user_name == correct_username and user_pass == correct_password:
    print('Login Successful')
# Else if only the entered_username matches but the password doesn't, print "Incorrect password."
elif user_name == correct_username and user_pass != correct_password:
    print('Incorrect Password')
# Else (if username doesn't match), print "Username not found."
else:
    print('Username Not Found')