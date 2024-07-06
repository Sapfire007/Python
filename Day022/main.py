letter = "Hey this is {} and I am from {}"
name = "Saptarshi Bose"
country = "India"
print(letter.format(name,country))
letter2 = "I love {1} and my favourite color is {0}"
hobby = "gaming"
color = "yellow"
print(letter2.format(color,hobby))
name2 = "Saptarshi"
age = 17
print(f"Hey this is {name2} and I'm currently {age} y/o")
print(f"We use f-strings like this : Hey this is {{name2}} and I'm currently {{age}} y/o")
txt = "For only {price:.2f}$ !"
print(txt.format(price=49.099999))
print(f"{2*30}")
print(type(f"{2*30}"))