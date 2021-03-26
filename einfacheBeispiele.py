# REPL = "Read Evaluate Print Loop"

# Variable für zwei Zahlen
x = 3
y = 5

# Rechnen mit Zahlen
z = x + y

# Ausgabe einer Variablen
print(z)

# Wiederverwenden von Variablen
# Python ist dynamisch getypt
z = "Hallo"
print(z)
print(type(z))

z = 3
print(type(z))

f = 3.5
print(f)
print(type(f))

# Eine Liste
l1 = [3,5,7,42,23,38]
print(l1)
print(l1[3])

# Slices von Listen
# l1[m:n]: halboffenes Intervall: [l[m], ... , l[n-1]]
print(l1[2:4])
print(l1[1:])

# For-Schleife
for el in l1:
  print(el)

for i in range(3,11,2):
  print(i)


# while True:
#  print("Hello World")
#  print("Its me Mario")




