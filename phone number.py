#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses in a block of text 

import re, pyperclip

#Step 1: Copy and paste the text to be searched 

#Step 2: Regexes for phone numbers and email addresses

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              #area code optional
    (\s|-|\.)?                      #separator optional as the area code may be in parentheses 
    (\d{3})                         #first 3 digits
    (\s|-|\.)                       #separator not optional
    (\d{4})                         #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension optional
    )''', re.VERBOSE)

#TODO Email regex

#Step 3: Find all matches of both regexes


#Step 4: Neatly format matched strings into a single string

#Copy that string to the clipboard

#Step 5: Display an apology if no matches are found 

#Step 2: create a Regex object using re.compile()
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
#Use a raw string for your regex so you do not have to escape the backslashes  

#Step 3: Pass a string into the Regex object's search() method
mo = phoneNumRegex.search('My number is 415-222-4242')
#This returns a Match object

#search() returns the first match
#findall() returns all matches as a list of strings
#OR if there are groups in the regex, it will return a list of tuples of strings!!! 

#Step 4: Call the Match object's group() method to return a string of matched text 
print('Phone number found: '  + mo.group())

#Combine steps:
print(phoneNumRegex.search('My number is 415-345-4242').group())
#prints the phone number


