Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> phoneRegex
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
>>> phoneRegex.search()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    phoneRegex.search()
TypeError: search() missing required argument 'string' (pos 1)
>>> phoneRegex.search('Your string here')  #search() method of regular expression data type and this would find the first match of the pattern in passed string.
>>> 
>>> phoneRegex.findall('Your String here') #findall() method of regular expression data type allows to search a string for all matches of regular expression pattern.
[]

>>> #search() returns Match Objects
>>> #findall() returns a list of strings
>>> 
>>> 
>>> resume = '''The Department of Telecommunications has divided India into various telecom circles such that within each circle, the call is treated as a local call, while across zones, it becomes a long-distance call. 508-555-5555. As of July 2018 there are 23 telecom circles or service areas. They are classified into four categories: Metro, A, B, C. 508-555-1234. Delhi, Mumbai, Kolkata and Chennai fall under Metro category.[1]'''
>>> 
>>> 
>>> phoneRegex.search(resume)
<re.Match object; span=(204, 216), match='508-555-5555'>
>>> phoneRegex.findall(resume)
['508-555-5555', '508-555-1234']
>>> 
>>> 
>>> phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
>>> phoneRegex.findall(resume)
[('508', '555-5555'), ('508', '555-1234')]
>>> 
>>> #findall() returns a list of strings when the pattern has 0 or 1 groups
>>> #findall() returns a list of tuple of strings when the pattern has 2 or more groups
>>> 
>>> 
>>> phoneRegex = re.compile(r'\d\d\d-(\d\d\d-\d\d\d\d)')
>>> phoneRegex.findall(resume)
['555-5555', '555-1234']
>>> 
>>> 
>>> phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
>>> phoneRegex.findall(resume)
[('508-555-5555', '508', '555-5555'), ('508-555-1234', '508', '555-1234')]
>>> [('508-555-5555', '508', '555-5555'), ('508-555-1234', '508', '555-1234')]
[('508-555-5555', '508', '555-5555'), ('508-555-1234', '508', '555-1234')]
>>> 
>>> 
>>> #divinding in to three groups - 1. Whole phone number 2. Area code 3. Main number results in each tuple with 3 strings
>>> 
>>> 
>>> #Character classes:
>>> #\d - Any numeric digit 0-9
>>> #\D - Any character that is not a numeric digit from 0-9
>>> #\w - Any letter, numeric digit or an underscore (Think of this as matching "word" characters)
>>> #\W - Any character that is not a letter, numeric digit, or the underscore character
>>> #\s - Any space, tab or new line character. (Think of this as matching "space" characters)
>>> #\S - Any character that is not a space, tab, or new line
>>> 
>>> lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing'
>>> xmasRegex = re.compile(r'\d+\s\w+')
>>> xmsRegex.findall(lyrics)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    xmsRegex.findall(lyrics)
NameError: name 'xmsRegex' is not defined
>>> xmasRegex.findall(lyrics)
['12 drummers', '11 pipers', '10 lords', '9 ladies']
>>> 
>>> 
>>> #We can create our own character classes
>>> vowelRegex = re.compile(r'[aeiouAEIOU]')  #equals to r'(a|e|i|o|u|A|E|I|O|U)'
>>> vowelRegex.findall('Robocop eats baby food.')
['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o']
>>> 
>>> vowelRegex = re.compile(r'[aeiouAEIOU]{2}') #match 2 consecutive vowels
>>> vowelRegex.findall('Robocop eats baby food.')
['ea', 'oo']
>>> 
>>> 
>>> vowelRegex = re.compile(r'[^aeiouAEIOU]')
>>> vowelRegex.findall('Robocop eats baby food.')
['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.']
>>> #The ^ tell to match any character that is not in the pattern.
>>> 
>>> #\d is a shorthand character class that matches digits. \w matches word characters. \s matches whitespace characters
>>> #the uppercase shorthand character classes \D,\W,\S match characters that are not digits, words and spaces
>>> 