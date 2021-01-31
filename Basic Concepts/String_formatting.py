Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

>>> #String formatting with reduced complexity
>>> 'hello ' + 'world'
'hello world'

>>> name = 'Alice'
>>> place = 'Main street'
>>> time = '6 pm'
>>> food = 'Pizza'

>>> 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
'Hello Alice, you are invited to a party at Main street at 6 pm. Please bring Pizza.'

>>> 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name,place,time,food)
'Hello Alice, you are invited to a party at Main street at 6 pm. Please bring Pizza.'

>>> 
