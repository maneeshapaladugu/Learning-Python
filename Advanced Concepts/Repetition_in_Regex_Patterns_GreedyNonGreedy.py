Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> #Repetition in Regex Patterns and GreedyNongreedy Matching:
>>> 
>>> #? (match zero or one time)
>>> #* (match 0 or more times)
>>> #+ (match 1 or more times)


>>> import re
>>> batRegex = re.compile(r'Bat(wo)?man') #wo apears zero or one time in the text in order to match the pattern Batman or Batwoman
>>> mo = batRegex.search('The adventures of Batman')
>>> mo.group()
'Batman'

>>> #The above string in broad :
>>> batRegex = re.compile(r'Batman|Batwoman')
>>> mo = batRegex.search('The adventures of Batwoman')
>>> mo.group()
'Batwoman'
>>> 
>>> 
>>> mo = batRegex.search('The adventures of Batwowowowman')
>>> mo == None
True
>>> 
>>> 
>>> 
>>> phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'


>>> mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
>>> mo.group()
'415-555-1234'


>>> mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow')
>>> mo.group()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    mo.group()
AttributeError: 'NoneType' object has no attribute 'group'

>>> mo == None
True

>>> #? helps to avoid the above error as shown here:
>>> phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
>>> phoneRegex.search('My phone number is 415-555-1234. call me tomorrow')
<re.Match object; span=(19, 31), match='415-555-1234'>

>>> phoneRegex.search('My phone number is 555-1234. call me tomorrow')
<re.Match object; span=(19, 27), match='555-1234'>


>>> 
>>> 
>>> ################################################################
>>> 
>>> #For example, if you wanted a regex object for the text "dinner?" (with the question mark), you would call: re.comple(r'dinnner\?') - note the slash in \? - In this case, dinner is not the optional. We are literally looking for a question mark: "dinner?"
>>> 
>>> batRegex = re.compile(r'Bat(wo)*man') #wo appears 0 or more times
>>> batRegex.search('The Adventures of Batman')
<re.Match object; span=(18, 24), match='Batman'>
>>> batRegex.search('The Adventures of Batwoman')
<re.Match object; span=(18, 26), match='Batwoman'>
>>> batRegex.search('The Adventures of Batwowowowowoman')
<re.Match object; span=(18, 34), match='Batwowowowowoman'>
>>> 
>>> 
>>> 
>>> 
>>> batRegex = re.compile(r'Bat(wo)+man') #wo appears 1 or more times
>>> batRegex.search('The Adventures of Batman') == None
True
>>> batRegex.search('The Adventures of Batwoman')
<re.Match object; span=(18, 26), match='Batwoman'>
>>> batRegex.search('The Adventures of Batwowowowowowoman')
<re.Match object; span=(18, 36), match='Batwowowowowowoman'>
>>> 
>>> 
>>> 
>>> #Escaping ?,*,+: If we literally want to match the characters like +,*,? which has a special meaning in regular expressions, we can just preceed them with a blackslash to Escape them.
>>> regex = re.compile(r'\+\*\?') #The pattern that we are looking for is a literal + sign, literal * sign and a literal ? sign
>>> regex.search('I learned about +*? regex syntax')
<re.Match object; span=(16, 19), match='+*?'>
>>> regex = re.compile(r'(\+\*\?)+')  # The + tells to match one or more of the preceeding group within the paranthesis
>>> regex.search('I learned about +*?+*?+*?+*?+*?+*?+*? regex syntax')
<re.Match object; span=(16, 37), match='+*?+*?+*?+*?+*?+*?+*?'>
>>> 
>>> 
>>> 
>>> #Exactly x - {x}:
>>> haRegex = re.compile(r'(Ha){3}')
>>> haRegex.search('He said "HaHaHa"')
<re.Match object; span=(9, 15), match='HaHaHa'>
>>> phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d=\d\d\d\d(,)?){3}')
>>> phoneRegex.search('My numbers are 415-555-1234,555-4242,222-555-0000')
>>> phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
>>> phoneRegex.search('My numbers are 415-555-1234,555-4242,222-555-0000')
<re.Match object; span=(15, 49), match='415-555-1234,555-4242,222-555-0000'>
>>> 
>>> 
>>> 
>>> #(at least x, at most y) - {x,y}
>>> haRegex = re.compile(r'(Ha){3,5}')
>>> haRegex.search('He said "HaHaHa"')
<re.Match object; span=(9, 15), match='HaHaHa'>
>>> haRegex.search('He said "HaHaHaHaHaHa"')
<re.Match object; span=(9, 19), match='HaHaHaHaHa'>
>>> haRegex.search('He said "HaHaHaHaHaHaHaHaHa"')
<re.Match object; span=(9, 19), match='HaHaHaHaHa'>
>>> haRegex = re.compile(r'(Ha){3,}') #at least 3, at most many
>>> haRegex = re.compile(r'(Ha){,5}') #at least 0, at most 5
>>>

>>> digitRegex = re.compile(r'(\d){3,5}')  #Greedy match
>>> digitRegex.search('1234567890')
<re.Match object; span=(0, 5), match='12345'>
>>> 
>>> 
>>> digitRegex = re.compile(r'(\d){3,5}?')  #Non Greedy match
>>> digitRegex.search('1234567890')
<re.Match object; span=(0, 3), match='123'>
>>> 
>>> 
>>> #Greedy match: Python tries to match the maximum longest possible string
>>> #Non Greedy match: Python tried to match the minimum smallest possible string. It can be achived using ? followed by the group {x,y}.
#The ? here is different from the meaning of 0 or more. Putting a ? after the curly braces makes it to do a nongreedy match.

