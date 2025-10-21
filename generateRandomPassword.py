
import string
import random

def lengthPassword():
    return int(input('Enter the length of the password string: '))

def generatepassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range (0,length))
    return password

def main():
    passwordlength = lengthPassword()
    generatedpassword = generatepassword(passwordlength)
    print ("password:", generatedpassword)

# calls main()
if (__name__=="__main__"):
    main()
