#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses in a block of text 

import re, pyperclip

#Step 1: Copy and paste the text to be searched 

#Step 2: Regexes for phone numbers and email addresses

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              
    (\s|-|\.)?
    (\d{3})                         
    (\s|-|\.)                       
    (\d{4})                         
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  
    )''', re.VERBOSE)
# Guide to groups: Area code with possible (); separator optional; 3 digits
# separator optional, 4 digits, optional extension 

#TODO Email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+ 
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

#No groups here because none of the components are optional

#Step 3: Find all matches of both regexes

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phoneNum += ' x' + groups[6] #Book says 8 instead of 6
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


#Step 4: Neatly format matched strings into a single string
#Copy that string to the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No contact info found.')




