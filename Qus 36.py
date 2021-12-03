#Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'polis' then add 'polisCSIT' instead.
#  If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcpolisCSIT'
# Sample String : 'Acropolis'
# Expected Result : 'AcropolisCSIT'
s = input("Enter a string: ")
if len(s) < 3:
 print("Invalid string.")
else:
 if s.endswith('polis'):
  print(s+'CSIT')
 else:
  print(s+'polisCSIT')
