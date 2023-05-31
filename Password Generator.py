import random

a = ["1","2","3","4","5","6","7","8","9","0"]
b = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
c = ["!","@","#","$","%","&"]

a1 = random.choice(a)
b1 = random.choice(b)
c1 = random.choice(c)

a2 = random.choice(a)
b2 = random.choice(b)
c2 = random.choice(c)

z = (a1 + b1 + c1 + a2 + b2 + c2)

print(f"Your password is {z}")