import random
import string
import time
start=time.time()
print(start)
passs=""
while True:
    def generate_password(length=8):
        # Define the character set to choose from
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate a random password
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

        # Generate and print the password
    random_password = generate_password()
    passs=passs+random_password+"\n"
    print(passs)
f=open("wifipass.txt",'w')
output=f.write(passs)
print(random_password)
f.close()



end=time.time()
print(end)
elasped=(end-start)/60
print("The Total Time Elasped is:",elasped,minutes)
