import random , string

length = int(input('please enter your length password : '))
passWord = string.ascii_letters + string.digits + '!@#$%^&*()'
powerfulPassword = "".join([random.choice(passWord) for i in range(length)])

print(f"your password is : {powerfulPassword}")