import os
import time
import sys
from cfonts import render
from termcolor import colored

banner = render("crypt buddy", colors=['blue', 'yellow'], align='center')
print(banner)

print('Warning: This tool is only a testing version.It performs only simple encryption...')

print("======================================================")

sos='Sources:-> github , stackoverflow'
print(colored(sos,'blue'))
cred='Coded and resembled by:--> @$um1t'
print(colored(cred,'yellow'))
lang='Made with love by Python'
print(colored(lang,'green'))
print("======================================================")

# encrypt and decrypt a text using a simple algorithm of offsetting the letters

key = 'abcdefghijklmnopqrstuvwxyz'



def encrypt(n, plaintext):

    """Encrypt the string and return the ciphertext"""

    result = ''



    for l in plaintext.lower():

        try:

            i = (key.index(l) + n) % 26

            result += key[i]

        except ValueError:

            result += l



    return result.lower()



def decrypt(n, ciphertext):

    """Decrypt the string and return the plaintext"""

    result = ''



    for l in ciphertext:

        try:

            i = (key.index(l) - n) % 26

            result += key[i]

        except ValueError:

            result += l



    return result

time.sleep(1)

text = str(input(colored('[*]  Enter a text or sentence to encrypt:--> ','green')))

offset = 5
time.sleep(1)
print("Loading:")

#animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

for i in range(len(animation)):
    time.sleep(0.3)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()

print("\n")


encrypted = encrypt(offset, text)

out='[+] your encrypted text is here:--> '
print(colored(out,'green'),encrypted)

time.sleep(1)

output = render('Thankyou!', colors=['yellow', 'red'], align='center')
print(output)



def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n [-] Do you want to restart this program ?(y/n) ")
    if answer.lower().strip() in "y".split():
        restart_program()