#! python3
# phoneAndEmail.py - finds phone numbers and email addresses on the clipboard
import pyperclip
import re
from hashlib import md5
import pwinput

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?              # area code
(\s|-|\.)?                      # separator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # separator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)s*(\d{2,5}))?   # extension 
)''', re.VERBOSE)

# Create Email regex.
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+               # username
@                               # @ symbol
[a-zA-Z0-9._%+-]+               # domain name
(\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)

# Find Matches in clipboard text.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

matches2 = []

paswrd = pwinput.pwinput()


for _ in matches:
    text = _
    output = md5(text.encode('utf-8'))
    print('Hash value:', output.hexdigest())
    matches2.append(output.hexdigest())


def passwordinput():
    count = 0

    while count != 5:
        prompt4 = pwinput.pwinput()
        if prompt4 != paswrd:
            print(f'incorrect password {4 - count} more tries')
            count += 1
        elif prompt4 == paswrd:
            encrypt3()
    if count == 5:
        quit()


def encrypt():
    prompt1 = input('Would you like to access numbers? yes or no: ')
    if prompt1 != 'no':
        passwordinput()
    elif prompt1 == 'no':
        quit()


def encrypt3():
    quest = input('enter encryption: ')
    for match in matches2:
        if quest == match:
            for match3 in matches:
                if matches2.index(match) == matches.index(match3):
                    print(match3)
                    encrypt()


encrypt()
