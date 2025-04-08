h1= int(input("coloque uma hora do dia: "))
m1 = int(input("digite os minutos dentro dessa hora: "))
h2 = int(input("coloque uma hora do dia: "))
m2 = int(input("digite os minutos dentro dessa hora: "))

somah = h1+h2
somam = m1+m2

if somam>59:
    somah += 1
    somam %= 60
if somah >36:
    somah-=36
elif somah>=24:
    somah-=24
elif somah>=12:
    somah-= 12
print(f"{somah}:{somam}")