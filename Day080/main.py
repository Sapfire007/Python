# Regular Expressions in Python
# https://regexr.com/

import re

pattern = "freshwater"
pattern2 = r"[A-Z]nited"
pattern3 = r"[A-Z|a-z]he"
text = ''' The Gowanus Canal is a 1.8-mile-long (2.9 km) canal in the New York City borough of Brooklyn, on the westernmost portion of Long Island. It was created in the mid–19th century from local tidal wetlands and freshwater streams, and by the end of that century was very polluted due to heavy industrial use. Most industrial tenants had stopped using the canal by the middle of the 20th century, but it remained one of the most polluted bodies of water in the United States. Its proximity to Manhattan and upper-class Brooklyn neighborhoods has attracted waterfront redevelopment in recent years, alongside attempts at environmental cleanup. It was designated a Superfund site in 2009. This five-segment panoramic photograph shows the Gowanus Canal as viewed from Union Street Bridge in 2021, looking northeastward towards Downtown Brooklyn. '''
match = re.search(pattern,text)
print(match)
if match:
  print("Match found!")

else:
  print("Match not found!")

print("\n")
match2 = re.search(pattern2,text)
print(match2)
if match2:
  print("Match found!")

else:
  print("Match not found!")

print("\n")
matches = re.finditer(pattern3,text)
print(matches)
for match3 in matches:
  print(match3)
  print(match3.span())
  print(type(match3))
  print(type(match3.span()))
  print(text[match3.span()[0]:match3.span()[1]])



"""
Regular Expressions in Python :
Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.
"""
"""
Metacharacters in regular expressions:
[]  Represent a character class
^   Matches the beginning
$   Matches the end
.   Matches any character except newline
?   Matches zero or one occurrence.
|   Means OR (Matches with any of the characters
    separated by it.
*   Any number of occurrences (including 0 occurrences)
+   One or more occurrences
{}  Indicate number of occurrences of a preceding RE 
    to match.
()  Enclose a group of REs

Find list of more meta characters here - https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions
"""

"""
Importing re Package :
In Python, regular expressions are supported by the re module. The basic syntax for working with regular expressions in Python is as follows:

import re

"""
"""
Searching for a pattern in re using re.search() Method :
re.search() method either returns None (if the pattern doesn’t match), or a re.MatchObject that contains information about the matching part of the string. This method stops after the first match, so this is best suited for testing a regular expression more than extracting data. We can use re.search method like this to search for a pattern in regular expression:

# Define a regular expression pattern
pattern = r"expression"

# Match the pattern against a string
text = "Hello, world!"

match = re.search(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")
"""
"""
Searching for a pattern in re using re.findall() Method :
You can also use the re.findall function to find all occurrences of the pattern in a string:

import re
pattern = r"expression"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']
"""
"""
Replacing a pattern :
The following example shows how to replace a pattern in a string:

import re
pattern = r"[a-z]+at"
text = "The cat is in the hat."

matches = re.findall(pattern, text)

print(matches)
# Output: ['cat', 'hat']

new_text = re.sub(pattern, "dog", text)

print(new_text)
# Output: "The dog is in the dog."
"""
r"""
Extracting information from a string :
The following example shows how to extract information from a string using regular expressions:

import re

text = "The email address is example@example.com."

pattern = r"\w+@\w+\.\w+"

match = re.search(pattern, text)

if match:
    email = match.group()
    print(email)
# Output: example@example.com
"""
"""
Conclusion : Regular expressions are a powerful tool for working with strings and text data in Python. Whether you're matching patterns, replacing text, or extracting information, regular expressions make it easy to perform complex string operations with just a few lines of code. With a little bit of practice, you'll be able to use regular expressions to solve all sorts of string-related problems in Python.
"""