name = "PRIYANSHIKASAUDHAN"

print(len(name))

print(name.startswith("PRI"))

print(name.endswith("DHAN"))

s = str(123)
print(s)
print(type(s))

#lower()

a ="HELLO"

l = a.lower()
print(l)

#UPPER

b ="hello"
print(b.upper())

#strip

c= "    hello     "
print(c.strip())

#replace(old,new)

d="hello world"
print(d.replace("world" , "Priyanshi"))

#split(delimiter)

e="apple,banana,orange"
print(e.split(","))

#join(iterable)

f=","
print(f.join(["apple","banana","orange"]))

#find(substring)

g="Priyanshi"
print(g.find("i"))

#startswith(prefix)

h ="priyanshi"
print(h.startswith("pri"))

#endswith(suffix)

i="hello"
print(i.endswith("lo"))

#Capitalize

j="priyanshi kasaudhan"
print(j.capitalize())

#count(subsstring)

k="qqqaaaabbbdssvfsdfsd"
print(k.count("A"))

#format

q="hello!  {}"
print(q.format("prishu"))

#isalpha

m="hello"
print(m.isalpha())