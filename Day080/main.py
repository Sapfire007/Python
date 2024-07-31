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