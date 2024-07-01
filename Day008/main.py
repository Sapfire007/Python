a = "Saptarshi"
print(len(a))
print(a.upper())
print(a.lower())
b = "!!!Hello!!!!!!!!!!!!!!!!!!!!"
print(b)
print(b.rstrip("!"))
c = "Express"
print(c)
print(c.replace("ss","ssion"))
d = "Cricket Football Hockey"
print(d.split(" "))
e = "hElLo theRe!"
print(e.capitalize())
f = "This text is centered."
print(f.center(50))
print(len(f))
print(len(f.center(50))) #Total number of characters including spaces
g = "Wassup!?"
print(g.endswith("?"))
h = "How are you ?"
print(h.endswith("are",4,7))
i = "Here is a python program and this is on String Methods"
print(i.find("is"))
print(i.index("is"))
print(i.find("dist"))
# print(i.index("dist")) this will give an error : ValueError: substring not found
print(i.isalnum())
j = "Hello009"
print(j.isalnum())
print(j.isalpha())
k = "Hi there!"
print(k.isalpha())
print((k[:2]).isalpha())
print((k[1:]).islower())
ll = "007"
print(ll.islower())
m = "yelloW"
print(m.islower())
print((m.replace("W","w007")).islower())
print((m.replace("W","w")).islower())
print(m.isprintable())
print((m+"\n").isprintable())
n = "                               "      #using spacebar
print(n.isspace())
o = "  " #using tab key
print(o.isspace())
p = "Central processing unit"
print(p.istitle())
q = "Central Processing Unit"
print(q.istitle())
print(q.isupper())
print((q.upper()).isupper())
print(q.startswith("central"))
print(q.startswith("Central"))
print(q.endswith("Unit"))
print(q.swapcase())
r = "iNdiAn premier LEAgue"
print(r)
print(r.title())