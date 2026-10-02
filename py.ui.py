import random 

characters="qwertyuiop[]\';lkjhgfdsa\zxcvbnm,./1234567890-=!@#$%^&*()_"
password=""
for i in range(18):
    password+=random.choice(characters)
print(password)