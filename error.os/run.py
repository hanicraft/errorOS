print "welcome to errorOS please login"
print "username : admin1"
print "password : error.os"

CorrectUsername = "admin1"
CorrectPassword = "error.os"

loop = 'true'
while (loop == 'true'):
    username = raw_input("Please enter your username: ")
    if (username == CorrectUsername):
    	password = raw_input("Please enter your password: ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
	else:
            print "Password incorrect!"
    else:
        print "Username incorrect!"


