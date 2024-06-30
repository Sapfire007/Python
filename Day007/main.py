a = "Saptarshi,Python"
print("The length of the string a : \"",a,"\" is = ",len(a))
print(a[0:9]) #including index of 0 but not 9
b = "Vortex"
print(b[1:3])
print(b[:]) #no boundaries
print(b[:4])
print(b[3:])
print(b[:-3]) #python interprets this as print(b[0:(len(b))-3])
print(b[-3:-1])